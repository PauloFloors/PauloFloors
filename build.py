"""
build.py — runs automatically on Netlify every time content changes
(including when Paulo adds/edits a photo through the admin panel).

It reads the editable photo files in /content/gallery-<service-slug>/
and rebuilds gallery_data.py, then regenerates every HTML page and the
sitemap using the same generator scripts used throughout this project.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

CONTENT_ROOT = "content"


def parse_frontmatter(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    fm = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip().strip('"')
        fm[key] = value
    return fm


def build_gallery_data():
    from service_data import SERVICES

    galleries = {}
    for svc in SERVICES:
        slug = svc["slug"]
        content_dir = os.path.join(CONTENT_ROOT, f"gallery-{slug}")
        photos = []
        if os.path.isdir(content_dir):
            entries = []
            for fname in os.listdir(content_dir):
                if not fname.endswith(".md"):
                    continue
                fm = parse_frontmatter(os.path.join(content_dir, fname))
                if not fm or "image" not in fm:
                    continue
                order = int(fm.get("order", 999))
                entries.append((order, fm["image"], fm.get("caption", "")))
            entries.sort(key=lambda e: e[0])
            # derive the folder name from the first image path, e.g.
            # /images/gallery/installation/installation-1.jpg -> installation
            folder = ""
            if entries:
                m = re.search(r"/images/gallery/([^/]+)/", entries[0][1])
                folder = m.group(1) if m else ""
            photos = [caption for _, _img, caption in entries]
        else:
            folder = ""
        galleries[slug] = {"folder": folder, "photos": photos}

    lines = ["GALLERIES = {"]
    for slug, data in galleries.items():
        lines.append(f'    "{slug}": {{')
        lines.append(f'        "folder": "{data["folder"]}",')
        lines.append('        "photos": [')
        for caption in data["photos"]:
            safe = caption.replace('"', '\\"')
            lines.append(f'            "{safe}",')
        lines.append("        ],")
        lines.append("    },")
    lines.append("}")

    with open("gallery_data.py", "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print("gallery_data.py rebuilt from /content")


def rebuild_sitemap():
    from city_data import CITIES, slugify
    from service_data import SERVICES

    base = "https://paulofloors.com"
    urls = [base + "/"]
    for s in SERVICES:
        urls.append(f"{base}/{s['slug']}/")
    for city, _ in CITIES:
        urls.append(f"{base}/hardwood-floors-in-{slugify(city)}-nj/")
    for s in SERVICES:
        for city, _ in CITIES:
            urls.append(f"{base}/{s['slug']}/{slugify(city)}-nj/")

    sitemap = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for u in urls:
        sitemap.append(f"  <url><loc>{u}</loc></url>")
    sitemap.append("</urlset>")

    with open("site/sitemap.xml", "w", encoding="utf-8") as f:
        f.write("\n".join(sitemap))

    print("sitemap.xml rebuilt —", len(urls), "urls")


def main():
    build_gallery_data()

    import importlib

    for mod_name in ["gen_service_pages", "gen_city_pages", "gen_service_city_pages"]:
        if mod_name in sys.modules:
            importlib.reload(sys.modules[mod_name])
        else:
            importlib.import_module(mod_name)

    rebuild_sitemap()
    print("BUILD COMPLETE")


if __name__ == "__main__":
    main()
