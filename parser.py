import sys
import xml.etree.ElementTree as ET
from datetime import datetime

# http://www.pythonlearn.com/html-007/cfbook014.html
tree = ET.parse(sys.argv[1])
root = tree.getroot()
with open('output.txt', 'w') as out:
	try:
		url = tree.find('required_header/url').text
	except:
		url = "N/A"
	out.write("%s\n" % url)

	try:
		nct_id = tree.find('id_info/nct_id').text
		nct_id = nct_id[3:]
	except:
		nct_id = "N/A"
	out.write("%s\n" % nct_id)

	try:
		brief_title = tree.find('brief_title').text
	except:
		brief_title = "N/A"
	out.write("%s\n" % brief_title)

	try:
		agency = tree.find('sponsors/lead_sponsor/agency').text
	except:
		agency = "N/A"
	out.write("%s\n" % agency)

	try:
		source = tree.find('source').text
	except:
		source = "N/A"
	out.write("%s\n" % source)

	try:
		overall_status = tree.find('overall_status').text
	except:
		overall_status = "N/A"
	out.write("%s\n" % overall_status)

	try:
		start_date = tree.find('start_date').text
	except:
		start_date = "N/A"
	if start_date != "N/A":
		temp_date = datetime.strptime(start_date, '%B %Y').strftime('%Y-%m-01')
		start_date = temp_date
		
	out.write("%s\n" % start_date)

	try:
		completion_date = tree.find('completion_date').text
	except:
		completion_date = "N/A"
        if completion_date != "N/A":
                temp_date = datetime.strptime(completion_date, '%B %Y').strftime('%Y-%m-01')
                completion_date = temp_date

	out.write("%s\n" % completion_date)

	try:
		phase = tree.find('phase').text
	except:
		phase = "N/A"
	out.write("%s\n" % phase)

	try:
		study_type = tree.find('study_type').text
	except:
		study_type = "N/A"
	out.write("%s\n" % study_type)

	try:
		primary_purpose = tree.find('study_design_info/primary_purpose').text
	except:
		primary_purpose = "N/A"
	out.write("%s\n" % primary_purpose)

	try:
		enrollment = tree.find('enrollment').text
	except:
		enrollment = "N/A"
	out.write("%s\n" % enrollment)

	try:
		condition = tree.find('condition').text
	except:
		condition = "N/A"
	out.write("%s\n" % condition)

	try:
		gender = tree.find('eligibility/gender').text
	except:
		gender = "N/A"
	out.write("%s\n" % gender)

	try:
		minimum_age = tree.find('eligibility/minimum_age').text
	except:
		minimum_age = "N/A"
	out.write("%s\n" % minimum_age)

	try:
		maximum_age = tree.find('eligibility/maximum_age').text
	except:
		maximum_age = "N/A"
	out.write("%s\n" % maximum_age)

	try:
		country = tree.find('location_countries/country').text
	except:
		country = "N/A"
	out.write("%s\n" % country)

	try:
		study_first_submitted = tree.find('study_first_submitted').text
	except:
		study_first_submitted = "N/A"

        if study_first_submitted != "N/A":
                temp_date = datetime.strptime(study_first_submitted, '%B %d, %Y').strftime('%Y-%m-%d')
                study_first_submitted = temp_date

	out.write("%s\n" % study_first_submitted)

	try:
		study_first_posted = tree.find('study_first_posted').text
	except:
		study_first_posted = "N/A"

        if study_first_posted != "N/A":
                temp_date = datetime.strptime(study_first_posted, '%B %d, %Y').strftime('%Y-%m-%d')
                study_first_posted = temp_date

	out.write("%s\n" % study_first_posted)

	try:
		last_update_submitted = tree.find('last_update_submitted').text
	except:
		last_update_submitted = "N/A"
        if last_update_submitted != "N/A":
                temp_date = datetime.strptime(last_update_submitted, '%B %d, %Y').strftime('%Y-%m-%d')
                last_update_submitted = temp_date
	out.write("%s\n" % last_update_submitted)

	try:
		list = tree.findall('keyword')
	except:
		list = "N/A"

	if list != "N/A":
		keyword = []
		for item in list:
			keyword.append(item.text)
	for word in keyword:
		out.write("%s\n" % word)


out.close()
