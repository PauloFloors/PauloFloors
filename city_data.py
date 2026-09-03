CITIES = [
    ("Aberdeen", "Monmouth"), ("Asbury Park", "Monmouth"), ("Atlantic Highlands", "Monmouth"),
    ("Belmar", "Monmouth"), ("Bradley Beach", "Monmouth"), ("Brielle", "Monmouth"),
    ("Cliffwood Beach", "Monmouth"), ("Colts Neck", "Monmouth"), ("Deal", "Monmouth"),
    ("Eatontown", "Monmouth"), ("Englishtown", "Monmouth"), ("Fair Haven", "Monmouth"),
    ("Farmingdale", "Monmouth"), ("Freehold", "Monmouth"), ("Hazlet", "Monmouth"),
    ("Highlands", "Monmouth"), ("Holmdel", "Monmouth"), ("Howell", "Monmouth"),
    ("Keyport", "Monmouth"), ("Leonardo", "Monmouth"), ("Lincroft", "Monmouth"),
    ("Little Silver", "Monmouth"), ("Long Branch", "Monmouth"), ("Manalapan", "Monmouth"),
    ("Manasquan", "Monmouth"), ("Marlboro", "Monmouth"), ("Matawan", "Monmouth"),
    ("Middletown", "Monmouth"), ("Millstone", "Monmouth"), ("Monmouth Beach", "Monmouth"),
    ("Neptune", "Monmouth"), ("Ocean Grove", "Monmouth"), ("Ocean Township", "Monmouth"),
    ("Oceanport", "Monmouth"), ("Red Bank", "Monmouth"), ("Rumson", "Monmouth"),
    ("Sea Bright", "Monmouth"), ("Sea Girt", "Monmouth"), ("Shrewsbury", "Monmouth"),
    ("Spring Lake", "Monmouth"), ("Tinton Falls", "Monmouth"),
    ("Brick", "Ocean"), ("Lavallette", "Ocean"), ("Ortley Beach", "Ocean"), ("Toms River", "Ocean"),
    ("East Brunswick", "Middlesex"), ("Monroe", "Middlesex"), ("Parlin", "Middlesex"),
    ("Sayreville", "Middlesex"), ("South River", "Middlesex"),
    ("Cranbury", "Mercer"), ("East Windsor", "Mercer"), ("Hightstown", "Mercer"),
    ("Jamesburg", "Mercer"), ("Lawrenceville", "Mercer"), ("Plainsboro", "Mercer"),
    ("Princeton", "Mercer"), ("Princeton Junction", "Mercer"), ("Robbinsville", "Mercer"),
    ("Roosevelt", "Mercer"), ("West Windsor", "Mercer"),
]

def slugify(name):
    special = {"Ocean Township": "ocean"}
    if name in special:
        return special[name]
    return name.lower().replace(" ", "-")

COUNTIES_ORDER = ["Monmouth", "Ocean", "Middlesex", "Mercer"]
