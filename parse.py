from bs4 import BeautifulSoup
import string
import re

infile = ""
outfile = ""

def parse_html(infile):
	
	#open the file
	str1 = open(infile, "r").read()
	output = ""
	#output = open(outfile, "w")

	soup = BeautifulSoup(str1)
	#print soup.prettify()
	#final_result = ""   #write all the infomation into one line
	#The store mode is name,location,summary,job_position,language,organization,course,project,skill,education,award,patent,group

	#get name
	name1 = soup.find_all("span", {'class':'full-name'})
	namestr = ""
	name = ""
	for i in range(0, name1.__len__()):
		namestr += str(name1[i])
		name2 = BeautifulSoup(namestr)
		name = name2.span.contents
	output+=("\n\n")
	output+=("name:")
	output+=(str(name) + "\t")

	#current industry
	current_sit2 = ""
	current_1 = soup.find_all("dd", {'class':'industry'})
	current_1str = ""
	for i in range(0, current_1.__len__()):
		current_1str += str(current_1[i])
		current_sit = re.sub("<dd class=\"industry\">", "", current_1str, 0) 
		current_sit2 = re.sub("</dd>", "", current_sit, 0)
	output+=("\ncurrent_industry:")
	output+=(str(current_sit2) + "\t")

	#good at
	good1 = soup.find_all("div", {'id':'headline-container'})
	good_name = []
	for i in range(0, good1.__len__()):
		good1str = str(good1[i])
		good2 = BeautifulSoup(good1str)
		if good2.p is not None:
			good_name = good2.p.contents
		else:
			good_name = []
	output+=("\ngood at: " + str(good_name) + "\t")

	#connection
	connection = ""
	conn = soup.find_all("div", {'class':'member-connections'})
	for i in range(0, conn.__len__()):
		connstr = str(conn)
		conn1 = BeautifulSoup(connstr)
		connection = conn1.strong.contents
	output+=("\nconnections" + str(connection) + "\t")

	#overview current background
	cu = soup.find_all("tr", {'id':'overview-summary-current'})
	current_overview = []
	for i in range(0, cu.__len__()):
		custr = str(cu[i])
		cu1 = BeautifulSoup(custr)
		current_overview = cu1.td.ol.li.contents
	output+=("\noverview current background: " + str(current_overview) + "\t")


	#overview previous background
	over1 = soup.find_all("tr", {'id':'overview-summary-past'})
	over7 = []
	if over1 is not None:
		over1str = ""
		for i in range(0,over1.__len__()):
			over1str += str(over1)
			over2 = BeautifulSoup(over1str)
			over3 = over2.td.ol
			over8 = str(over3)
			for j in range(0, over3.__len__()):
				over4 = re.sub("<li>", "", over8, 0)
				over5 = re.sub("</li>", "", over4, 0)
				over6 = re.sub("<ol>", "", over5, 0)
				over7 = re.sub("</ol>", "", over6, 0)
	else:
		over1 = []
	output+=("\noverview previous background: " + str(over7) + "\t")

	#overview education
	ee = soup.find_all("tr", {'id':'overview-summary-education'})
	over_edu = []
	for i in range(0, ee.__len__()):
		eestr = str(ee[i])
		ee1 = BeautifulSoup(eestr)
		ee1str = ee1.find_all("a", {'title':'More details for this school'})
		if BeautifulSoup( str(ee1str)).a is not None:
			over_edu = BeautifulSoup( str(ee1str)).a.contents
		else:
			over_edu = ""

	output+=("\noverview education :" + str(over_edu) + "\t")

	#get the location
	location = soup.find_all("div", {'id':'location-container'})
	locationstr = ""
	for i in range(0, location.__len__()):
		locationstr += str(location[i])
	locationsoup = BeautifulSoup(locationstr)
	locationresult = locationsoup.find_all("span", "locality")
	locationresultstr = ""
	for i in range(0, locationresult.__len__()):
		locationresultstr += str(locationresult[i])
	locationresultsoup = BeautifulSoup(locationresultstr)
	final_location = ""
	if locationresultsoup.span is not None:
		final_location = locationresultsoup.span.contents
	else:
		final_location = []
	output+=("\nlocation: " + str(final_location) + "\t")

	#get the summary
	summ = soup.find_all("div", {"class": "summary"})
	summstr = ""
	for i in range(0, summ.__len__()):
		summstr += str(summ[i])
	summstr = summstr.replace('<br/>', ' ')
	summstr = summstr.replace('\n', '')
	summstr = summstr.replace('</p></div>', '')
	summstr = summstr.replace('<div class="summary"><p class="description">', '')
	summary = summstr
	output+=("\nsummary: " + summary + "\t")

	#experience job position
	job_position = soup.find_all("div",{'id': 'background-experience-container'})
	jobstr = ""
	job_area3 = []
	job_time = ""
	jnumber = 0

	for i in range(0, job_position.__len__()):
		jobstr += str(job_position[i])
		jobsoup = BeautifulSoup(jobstr)
		#print jobsoup.prettify()
		jobsoupstr = jobsoup.find_all("div", {'class':'editable-item section-item past-position'})
		for j in range(0, jobsoupstr.__len__()):
			job2 = str(jobsoupstr[j])
			job2str = BeautifulSoup(job2)
			
			job3str = job2str.find_all("header")	
			for u in range(0, job3str.__len__()):
				jnumber = jnumber + 1
				job3 = str(job3str[u])
				job4 = BeautifulSoup(job3)
				job_list = job4.find_all('h5')
				#print job4.prettify()
				for h in range(0, job_list.__len__()):
					job5 = str(job_list[h])
					job5str = BeautifulSoup(job5)
					if job5str.h5.a is not None:
						job_organ = job5str.h5.a.contents
					elif job5str.h5 is not None:
						job_organ = job5str.h5.contents #judge whether the company have a logo
					else:
						job_organ = []
					jobtime = job2str.find_all("span", {'class':'experience-date-locale'})
					for k in range(0, jobtime.__len__()):
						jobtimestr = str(jobtime[k])
						jobtime2 = BeautifulSoup(jobtimestr)
						jobtime2str = jobtime2.find_all("time")
						jobtime3 = ""
						for b in range(0, jobtime2str.__len__()):
							jobtime3 += str(jobtime2str[b])
							jobtime3 = re.sub("<time>", "", jobtime3, 0) 
							jobtime3 = re.sub("</time>", "-", jobtime3, 0)
							job_time = jobtime3				

						job_area = jobtime2.find_all("span", {'class':'locality'})
						for p in range(0, job_area.__len__()):
							job_areastr = str(job_area[p])
							job_area2 = BeautifulSoup(job_areastr)
							if job_area2.span is not None:
								job_area3 = job_area2.span.contents
							else:
								job_area3 = ""

			if job2str.h4 is not None:
				job_name = job2str.h4.contents
			else:
				job_name = []

			#iif job2str is not None:
			#	job_time = job2str.time.contents
			#else:
			#	job_time = []
			if job2str.p is not None:
				job_content = job2str.p.contents
			else:
				job_content = []
			output+=("\njob name:" + str(job_name) + "\t" + "\njob area:"  + str(job_area3) + "\t" + "\njob company:" + str(job_organ) + "\t" + "\njob period:" + str(job_time) + "\t" + "\njob content:" + str(job_content) + "\t")
		output+=("\n" + "experience_number:" + str(jnumber + 1) + "\t\n")

		#current job
		jobsoupstr = jobsoup.find_all("div", {'class':'editable-item section-item current-position'})
		for j in range(0, jobsoupstr.__len__()):
			job2 = str(jobsoupstr[j])
			job2str = BeautifulSoup(job2)
			
			job3str = job2str.find_all("header")	
			for u in range(0, job3str.__len__()):
				job3 = str(job3str[u])
				job4 = BeautifulSoup(job3)
				job_list = job4.find_all('h5')
				#print job4.prettify()
				for h in range(0, job_list.__len__()):
					job5 = str(job_list[h])
					job5str = BeautifulSoup(job5)
					if job5str.h5.a is not None:
						job_organ = job5str.h5.a.contents
					elif job5str.h5 is not None:
						job_organ = job5str.h5.contents #judge whether the company have a logo
					else:
						job_organ = []
					jobtime = job2str.find_all("span", {'class':'experience-date-locale'})
					for k in range(0, jobtime.__len__()):
						jobtimestr = str(jobtime[k])
						jobtime2 = BeautifulSoup(jobtimestr)
						jobtime2str = jobtime2.find_all("time")
						jobtime3 = ""
						for b in range(0, jobtime2str.__len__()):
							jobtime3 += str(jobtime2str[b])
							jobtime3 = re.sub("<time>", "", jobtime3, 0) 
							jobtime3 = re.sub("</time>", "-", jobtime3, 0)
							job_time = jobtime3				

						job_area = jobtime2.find_all("span", {'class':'locality'})
						for p in range(0, job_area.__len__()):
							job_areastr = str(job_area[p])
							job_area2 = BeautifulSoup(job_areastr)
							if job_area2.span is not None:
								job_area3 = job_area2.span.contents
							else:
								job_area3 = ""

			if job2str.h4 is not None:
				job_name = job2str.h4.contents
			else:
				job_name = []

			#iif job2str is not None:
			#	job_time = job2str.time.contents
			#else:
			#	job_time = []
			if job2str.p is not None:
				job_content = job2str.p.contents
			else:
				job_content = []
			output+=("\ncurrent job name:" + str(job_name) + "\t" + "\ncurrent job area:" + str(job_area3) + "\t" + "\ncurrent job company:" + str(job_organ) + "\t" + "\ncurrent job period:" + str(job_time) + "\t" + "\ncurrent job content:" + str(job_content) + "\t")



	#get the language
	lang = soup.find_all("div", {'id':'background-languages-container'})
	langstr = ""
	for i in range(0, lang.__len__()):
		langstr += str(lang[i])
	lang2 = BeautifulSoup(langstr)
	lang3 = lang2.find_all('h4')
	for i in range(0, lang3.__len__()):
		lang3str = ""
		lang3str = str(lang3[i])
		lang4 = BeautifulSoup(lang3str)
		if lang4.h4 is not None:
			lang4str = lang4.h4.contents
		else:
			lang4str = []
		output+=("\nlanguage:" + str(lang4str) + "\t")

	#get the organization
	organization = soup.find_all("div", {'id':'background-organizations'})
	for i in range(0, organization.__len__()):
		organizationstr = str(organization)
		organ = BeautifulSoup(organizationstr)
		if organ.span is not None:
			organ_tstr = organ.span.contents
		else:
			organ_tstr = ""
		organ_tim = re.sub("<time>", "", str(organ_tstr), 0)
		organ_time = re.sub("</time>", "-", str(organ_tim), 0)

		if organ.h4 is not None:
			organ_name = organ.h4.contents
		else:
			organ_name = []
		if organ.h5 is not None:
			organ_place = organ.h5.contents
		else:
			organ_place = []
		organ_content = organ.find_all("p", {'class':'description'})
		output+=("\norganization: " + str(organ_name) + "\t" + str(organ_place) + "\t" + str(organ_time) + "\t" + str(organ_content) + "\t")

	#get the course
	course = soup.find_all("div", {'id':'background-courses-container'})
	coursestr = ""
	for i in range(0, course.__len__()):
		coursestr += str(course[i])
	course2 = BeautifulSoup(coursestr)
	course3 = course2.find_all('li')
	for i in range(0, course3.__len__()):
		course3str = ""
		course3str = str(course3[i])
		course4 = BeautifulSoup(course3str)
		if course4.li is not None:
			course4str = course4.li.contents
		else:
			course4str = []
		output+=("\ncourse: " + str(course4str) + "\t")

	#get the project
	project = soup.find_all("div", {'id':'background-projects'})
	for i in range(0, project.__len__()):
		projectstr = str(project[i])
		project2 = BeautifulSoup(projectstr)
		project2str = project2.find_all("div", {'class':'editable-item section-item'})
		#print project2.prettify()
		for j in range(0, project2str.__len__()):
			project3 = str(project2str[j])
			project3str = BeautifulSoup(project3)
			if project3str.h4.a is not None:
				project_name = project3str.h4.a.contents
			elif project3str.h4.a is not None:
				project_name = project3str.h4.contents
			else:
				project_name = []
			if project3str.time is not None:
				project_time = project3str.time.contents
			else:
				project_time = ""
			if project3str.p is not None:
				project_content = project3str.p.contents
			else:
				project_content = ""
			output+=("\nproject name:" + str(project_name) + "\t" + "\nproject time:" + str(project_time) + "\t" + "\nproject content:" + str(project_content) + "\t")

	#get the skills
	skill = soup.find_all("div", {'id':'background-skills-container'})
	skillstr = ""
	for i in range(0, skill.__len__()):
		skillstr += str(skill[i])
	skill2 = BeautifulSoup(skillstr)
	skill2str = skill2.find_all("span", {'class':'endorse-item-name-text'})
	skill_num = skill2str.__len__()
	output+=("\n" + "skill_num:" + str(skill2str.__len__()) + "\n")
	for i in range(0, skill2str.__len__()):
		skill3 = str(skill2str[i])
		skill3str = BeautifulSoup(skill3)
		if skill3str is not None:
			skill4 = skill3str.span.contents
		else:
			skill4 = []
		output+=("\nskills:" + str(skill4) + "\t")


	#get the education
	edu4_num = 0
	edu = soup.find_all("div", {'id':'background-education-container'})
	for i in range(0, edu.__len__()):
		edustr = str(edu[i])
		edu1 = BeautifulSoup(edustr)
		#print edu1.prettify()
		edu1str = edu1.find_all("div", {'id':'background-education'})
		for j in range(0, edu1str.__len__()):
			edu2 = str(edu1str[j])
			edu2str = BeautifulSoup(edu2)
			edu3 = edu2str.find_all("div", {'class':'editable-item section-item'})
			output += ("\n" + "education_nun:" + str(edu3.__len__()) + "\t\n")
			for k in range(0, edu3.__len__()):
				edu3str = str(edu3[k])
				edu4 = BeautifulSoup(edu3str)
				edu4_school_detail = edu4.find_all("a", {'title':'More details for this school'})
				edu4_schoolstr1 = ""
				for u in range(0, edu4_school_detail.__len__()):
					edu4_school = str(edu4_school_detail[u])
					edu4_schoolstr = BeautifulSoup(edu4_school)
					if edu4_schoolstr.a is not None:
						edu4_schoolstr1 = str(edu4_schoolstr.a.contents)
					else:
						edu4_schoolstr1 = ""
				
				edu4_major = edu4.find_all("a", {'title':'Explore this field of study'})
				edu4_majorstr1 = ""
				edu4_num = edu4_major.__len__()
				#print "major number " + str(edu4_num)
				for g in range(0, edu4_num):
					edu4_major3 = str(edu4_major[g])
					edu4_majorstr = BeautifulSoup(edu4_major3)
					if edu4_majorstr.a is not None:
						edu4_majorstr1 = str(edu4_majorstr.a.contents)
					else:
						edu4_majorstr1 = ""
				
				edu4_t = edu4.find_all("span", {'class':'education-date'})
				edu4_tstr = ""
				for w in range(0, edu4_t.__len__()):
					edu4_tstr += str(edu4_t[w])
					edu5_t = BeautifulSoup(edu4_tstr)
					edu_tim = edu5_t.span.contents
					edu_tim1 = re.sub("<time>", "", str(edu_tim), 0)
					edu_time = re.sub("</time>", "", str(edu_tim1), 0)

				output+=("\neducation school:" + edu4_schoolstr1 + "\t" + "\neducation major:" + edu4_majorstr1 + "\t" + "\neuducation time:" + str(edu_time))


	#get the awards
	honor = soup.find_all("div", {'id':'background-honors-container'})
	for i in range(0, honor.__len__()):
		honorstr = str(honor[i])
		honor2 = BeautifulSoup(honorstr)
		#print honor2.prettify()
		honor3 = honor2.find_all("div", {'class':'editable-item section-item'})
		for j in range(0, honor3.__len__()):
			honor3str = str(honor3[j])
			honor4 = BeautifulSoup(honor3str)
			if honor4.h4 is not None:
				honor5_name = honor4.h4.contents
			else:
				honor5_name = []
			if honor4.time is not None:
				honor5_time = honor4.time.contents
			else:
				honor5_time = []
			if honor4.p is not None:
				honor5_des = honor4.p.contents
			else:
				honor5_des = []
			output+=("\nhonor name:" + str(honor5_name) + "\t" + "\nhonor time:" + str(honor5_time) + "\t" + "\nhonor content:" + str(honor5_des) + "\t")

	#get the patents
	patent = soup.find_all("div", {'id':'background-patents-container'})
	for i in range(0, patent.__len__()):
		patentstr = str(patent[i])
		patent2 = BeautifulSoup(patentstr)
		#print patent2.prettify()
		patent3 = patent2.find_all("div", {'class':'editable-item section-item'})
		for j in range(0, patent3.__len__()):
			patent3str = str(patent3[j])
			patent4 = BeautifulSoup(patent3str)
			if patent4.h4 is not None:
				patent4_name = patent4.h4.contents
			else:
				patent4_name = ""
			if patent4.h5 is not None:
				patent4_place = patent4.h5.contents
			else:
				patent4_place = ""
			if patent4.span is not None:
				patent4_time = patent4.span.contents
			else:
				patent4_time = ""
			if patent4.dt is not None:
				patent4_num = patent4.dt.contents
			else:
				patent4_num = ""
			output+=("\npatent name:" + str(patent4_name) + "\t" + "\npatent place:" + str(patent4_place) + "\t" + "\npatent time:" + str(patent4_time) + "\t" + "\npatent number:" + str(patent4_num) + "\t")


	#get the group
	group = soup.find_all("div", {'id':'groups-container'})
	for i in range(0, group.__len__()):
		groupstr = str(group[i])
		group2 = BeautifulSoup(groupstr)
		group2str = group2.find_all('strong')
		group_num = group2str.__len__()
		for i in range(0, group_num):
			groupstr = str(group2str[i])
			group1 = BeautifulSoup(groupstr)
			if group1.strong is not None:
				group1str = group1.strong.contents
			else:
				group1str = ""
			output+=("\ngroup: " + str(group1str) + "\n")

	#write the number of the people have three
	if(jnumber != 0 and skill_num != 0 and edu4_num != 0):
		output+=("\nthree:" + "1" + "\n")
	else:
		output+=("\nthree:0\n")

	return output
