import sys
import xml.etree.ElementTree as ET

#with open(sys.argv[1], 'r') as input:
#	data = input.read()
#	tree = ET.fromstring(data)

tags = ["required_header/url",
"id_info/nct_id",
"brief_title",
"sponsors/lead_sponsor/agency",
"source",
"overall_status",
"start_date",
"completion_date",
"phase",
"study_type",
"study_design_info/primary_purpose",
"enrollment",
"condition",
"eligibility/gender",
"eligibility/minimum_age",
"eligibility/maximum_age",
"location_countries/country",
"study_first_submitted",
"study_first_posted",
"last_update_submitted"]

# value = tree.find('tag').text
# http://www.pythonlearn.com/html-007/cfbook014.html
data = []
tree = ET.parse(sys.argv[1])
root = tree.getroot()

for item in tags:
	try:
		data.append(tree.find(item).text)
	except:
		print(item, " not found")

with open('output.txt', 'w') as out:
	for item in data:
		out.write("%s\n" % item) 
