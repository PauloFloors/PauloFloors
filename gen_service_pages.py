import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from service_data import SERVICES
from service_content import WHY_MATTERS
from gallery_data import GALLERIES
import template_builder as tb

OUT_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'site')

count = 0
for svc in SERVICES:
    slug = svc['slug']
    name = svc['name']
    gdata = GALLERIES.get(slug, {"folder": "", "photos": []})
    hero_img = (
        f"/images/gallery/{gdata['folder']}/{gdata['folder']}-1.jpg"
        if gdata['photos'] else "/images/hero-new.jpg"
    )

    breadcrumb_extra = (
        f'{{"@type": "ListItem", "position": 2, "name": "{name}", '
        f'"item": "https://paulofloors.com/{slug}/"}}'
    )

    page = tb.build_page(
        title=f"{name} in New Jersey | Paulo Floors",
        meta_description=f"{svc['short']} Serving homeowners throughout New Jersey. Get a free quote from Paulo Floors.",
        canonical=f"https://paulofloors.com/{slug}/",
        service_name=name,
        area_served="New Jersey",
        breadcrumb_extra=breadcrumb_extra,
        hero_img=hero_img,
        breadcrumb_trail=f"/ {name}",
        h1=name,
        intro=svc['intro'],
        process_heading=f"The Right Way to Handle {name}",
        slug=slug,
        why_matters=WHY_MATTERS.get(slug, ""),
        gallery_heading=f"{name} projects.",
        faq_heading=f"{name} FAQ",
        area_heading="Serving homeowners across New Jersey.",
        cta_heading=f"Got a {name.lower()} project in mind?",
    )

    folder = os.path.join(OUT_ROOT, slug)
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(page)
    count += 1

print("generated", count, "rich service pages")
