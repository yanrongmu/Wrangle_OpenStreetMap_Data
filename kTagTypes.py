import xml.etree.cElementTree as ET
import pprint
import re

lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

def key_type(element, keys):
    if element.tag == "tag":
        val = element.get("k")
        if bool(lower.search(val)):
            keys["lower"] += 1
        elif bool(lower_colon.search(val)):
            keys["lower_colon"] += 1
        elif bool(problemchars.search(val)):
            keys["problemchars"] += 1
        else:
            keys["other"] += 1
        pass
        
    return keys

def process_map(filename):
    keys = {"lower": 0, "lower_colon": 0, "problemchars": 0, "other": 0}
    for _, element in ET.iterparse(filename):
        keys = key_type(element, keys)

    return keys

keys = process_map('berkeley_california.osm')
pprint.pprint(keys)