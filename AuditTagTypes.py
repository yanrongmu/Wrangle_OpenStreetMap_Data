import xml.etree.cElementTree as ET
import pprint

def count_tags(filename):
    file = open(filename, "r")
    tags = {}
    for event, elem in ET.iterparse(file):
        if elem.tag in tags.keys():
            tags[elem.tag] += 1
        else:
            tags[elem.tag] = 1
    return tags

tags = count_tags('berkeley_california.osm')
pprint.pprint(tags)