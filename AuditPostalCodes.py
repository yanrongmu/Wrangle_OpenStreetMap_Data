import xml.etree.cElementTree as ET
import re
import pprint

OSMFILE = "berkeley_california.osm"

def audit_zipcode(zip_codes, zipcode_name):
    if not (re.match(r'^(947)\d{2}$', zipcode_name)):
        if zipcode_name not in zip_codes:
            zip_codes[zipcode_name] = 1
        else:
            zip_codes[zipcode_name] += 1

def audit(osmfile):
	osm_file = open(osmfile, "r")
	zip_codes = {}
	for event, elem in ET.iterparse(osm_file, events=("start",)):
		if elem.tag == "node" or elem.tag == "way":
			for tag in elem.iter("tag"):
				if tag.attrib['k'] == "addr:postcode":
					audit_zipcode(zip_codes, tag.attrib['v'])
	elem.clear()
	return zip_codes

zipcodes = audit(OSMFILE)
pprint.pprint(dict(zipcodes))