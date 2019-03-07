import sys
import xml.etree.ElementTree as ET

with open(sys.argv[1], 'r') as input:
	data = input.read()
	tree = ET.fromstring(data)

tags = ["url",
"nct_id",
"brief_title",
"agency",
"source",
"overall_status",
"start_date",
"completion_date",
"phase",
"study_type",
"primary_purpose",
"enrollment",
"condition",
"gender",
"minimum_age",
"maximum_age",
"country",
"study_first_submitted",
"study_first_posted",
"last_update_submitted"]

# value = tree.find('tag').text
# http://www.pythonlearn.com/html-007/cfbook014.html

output = open('output.txt', 'a')
output.write(data) 
output.close()