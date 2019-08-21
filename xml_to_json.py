import json
import xmljson
from lxml.etree import parse

for x in ['articles', 'article_tags', 'departments', 'brands', 'schools', 'schools1', 'schools2', 'search_area', 'search_station', 'search_station1', 'areas_lines']:
    tree = parse(f"/Users/yamashitasatoshi/Downloads/{x}.xml")
    root = tree.getroot()

    with open(f"{x}.json", 'w') as fw:
        json.dump(xmljson.yahoo.data(root), fw, indent=2)
