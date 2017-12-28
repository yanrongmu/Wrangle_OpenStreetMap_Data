import xml.etree.cElementTree as ET

OSMFILE = "berkeley_california.osm"

def audit_zipcodes(osmfile):
    # iter through all zip codes, collect all the zip codes that does not start with 02
    osm_file = open(osmfile, "r")
    zip_codes = {}
    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if tag.attrib['k'] == "addr:postcode" and not tag.attrib['v'].startswith('947'):
                    if tag.attrib['v'] not in zip_codes:
                        zip_codes[tag.attrib['v']] = 1
                    else:
                        zip_codes[tag.attrib['v']] += 1
    return zip_codes

zipcodes = audit_zipcodes(OSMFILE)

for zipcode in zipcodes:
    print zipcode, zipcodes[zipcode]