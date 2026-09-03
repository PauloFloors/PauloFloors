import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from service_data import SERVICES
from service_content import WHY_MATTERS
from gallery_data import GALLERIES
from city_data import CITIES, slugify
import template_builder as tb

OUT_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'site')

county_labels = {
    "Monmouth": "Monmouth County",
    "Ocean": "Ocean County",
    "Middlesex": "Middlesex County",
    "Mercer": "Mercer County",
}

count = 0
for svc in SERVICES:
    slug = svc['slug']
    name = svc['name']
    gdata = GALLERIES.get(slug, {"folder": "", "photos": []})
    hero_img = (
        f"/images/gallery/{gdata['folder']}/{gdata['folder']}-1.jpg"
        if gdata['photos'] else "/images/hero-new.jpg"
    )

    for city, county in CITIES:
        city_slug = slugify(city)
        county_label = county_labels[county]
        page_slug = f"{city_slug}-nj"

        breadcrumb_extra = (
            f'{{"@type": "ListItem", "position": 2, "name": "{name}", '
            f'"item": "https://paulofloors.com/{slug}/"}},\n'
            f'    {{"@type": "ListItem", "position": 3, "name": "{city}, NJ", '
            f'"item": "https://paulofloors.com/{slug}/{page_slug}/"}}'
        )

        page = tb.build_page(
            title=f"{name} in {city}, NJ | Paulo Floors",
            meta_description=f"{svc['short']} Serving {city} and homeowners throughout {county_label}, New Jersey. Get a free quote from Paulo Floors.",
            canonical=f"https://paulofloors.com/{slug}/{page_slug}/",
            service_name=name,
            area_served=f"{city}, NJ",
            breadcrumb_extra=breadcrumb_extra,
            hero_img=hero_img,
            breadcrumb_trail=f"/ {name} / {city}, NJ",
            h1=f"{name} in {city}, NJ",
            intro=f"Paulo Floors provides {name.lower()} for homeowners in {city} and throughout {county_label}. {svc['intro']}",
            process_heading=f"The Right Way to Handle {name}",
            slug=slug,
            why_matters=WHY_MATTERS.get(slug, ""),
            gallery_heading=f"{name} projects.",
            faq_heading=f"{name} FAQ",
            area_heading=f"Also serving {county_label}.",
            cta_heading=f"Got a {name.lower()} project in {city}?",
            related_base_prefix="",
            area_city=city,
        )

        folder = os.path.join(OUT_ROOT, slug, page_slug)
        os.makedirs(folder, exist_ok=True)
        with open(os.path.join(folder, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(page)
        count += 1

print("generated", count, "service x city pages")
