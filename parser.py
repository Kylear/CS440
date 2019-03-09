import sys
import xml.etree.ElementTree as ET
from datetime import datetime

# http://www.pythonlearn.com/html-007/cfbook014.html
tree = ET.parse(sys.argv[1])
root = tree.getroot()
try:
	url = tree.find('required_header/url').text
except:
	url = "N/A"

try:
	nct_id = tree.find('id_info/nct_id').text
	nct_id = nct_id[3:]
except:
	nct_id = "N/A"

try:
	brief_title = tree.find('brief_title').text
except:
	brief_title = "N/A"

try:
	agency = tree.find('sponsors/lead_sponsor/agency').text
except:
	agency = "N/A"

try:
	source = tree.find('source').text
except:
	source = "N/A"

try:
	overall_status = tree.find('overall_status').text
except:
	overall_status = "N/A"

try:
	start_date = tree.find('start_date').text
	if start_date == "N/A":
		start_date = "NULL"
	else:
		temp_date = datetime.strptime(start_date, '%B %Y').strftime('%Y-%m-01')
		start_date = temp_date
except:
	start_date = "NULL"

try:
	completion_date = tree.find('completion_date').text
	if completion_date == "N/A":
		completion_date = "NULL"
	else:
		temp_date = datetime.strptime(completion_date, '%B %Y').strftime('%Y-%m-01')
		completion_date = temp_date
except:
	completion_date = "NULL"

try:
	phase = tree.find('phase').text
except:
	phase = "N/A"

try:
	study_type = tree.find('study_type').text
except:
	study_type = "N/A"

try:
	primary_purpose = tree.find('study_design_info/primary_purpose').text
except:
	primary_purpose = "N/A"

try:
	enrollment = tree.find('enrollment').text
	if enrollment == "N/A":
		enrollment = "NULL"
except:
	enrollment = "NULL"

try:
	condition = tree.find('condition').text
except:
	condition = "N/A"

try:
	gender = tree.find('eligibility/gender').text
except:
	gender = "N/A"

try:
	minimum_age = tree.find('eligibility/minimum_age').text
	if minimum_age == "N/A":
		minimum_age = "NULL"
	else:
		minimum_age = minimum_age[:-6]
except:
	minimum_age = "NULL"

try:
	maximum_age = tree.find('eligibility/maximum_age').text
	if maximum_age == "N/A":
		maximum_age = "NULL"
	else:
		maximum_age = maximum_age[:-6]
except:
	maximum_age = "NULL"

try:
	country = tree.find('location_countries/country').text
except:
	country = "N/A"

try:
	study_first_submitted = tree.find('study_first_submitted').text
	if study_first_submitted == "N/A":
		study_first_submitted = "NULL"
	else:
		temp_date = datetime.strptime(study_first_submitted, '%B %d, %Y').strftime('%Y-%m-%d')
		study_first_submitted = temp_date
except:
	study_first_submitted = "NULL"

try:
	study_first_posted = tree.find('study_first_posted').text
	if study_first_posted == "N/A":
		study_first_posted = "NULL"
	else:
		temp_date = datetime.strptime(study_first_posted, '%B %d, %Y').strftime('%Y-%m-%d')
		study_first_posted = temp_date
except:
	study_first_posted = "NULL"

try:
	last_update_submitted = tree.find('last_update_submitted').text
	if last_update_submitted == "N/A":
		last_update_submitted = "NULL"
	else:
		temp_date = datetime.strptime(last_update_submitted, '%B %d, %Y').strftime('%Y-%m-%d')
		last_update_submitted = temp_date
except:
	last_update_submitted = "NULL"

try:
	list = tree.findall('keyword')
except:
	list = "N/A"

if list != "N/A":
	keywords = []
	for item in list:
		keywords.append(item.text)


script = open('fill_tables.sql', 'a')

trials_sql = "INSERT INTO `trials` VALUES ("+nct_id+",'"+url+"','"+brief_title+"','"+agency+"','"+source+"','"+overall_status+"','"+start_date+"','"+completion_date+"','"+phase+"','"+study_type+"','"+primary_purpose+"',"+enrollment+",'"+condition+"','"+gender+"',"+minimum_age+","+maximum_age+",'"+country+"','"+study_first_submitted+"','"+study_first_posted+"','"+last_update_submitted+"');\n"

script.write(trials_sql)

for word in keywords:
	keywords_sql = "INSERT INTO `keywords` (study_id, keyword) VALUES ("+nct_id+",'"+word+"');\n"
	script.write(keywords_sql)

script.close()