import xml.etree.cElementTree as ET
import pprint

def get_user(element):
    if element.get('uid'):
        uid = element.attrib["uid"]
        return uid
    else:
        return None
    
def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        if get_user(element):
            users.add(get_user(element))
        pass

    return users

users = process_map('berkeley_california.osm')
pprint.pprint(users)
print(len(users))
