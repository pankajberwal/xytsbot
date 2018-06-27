from robobrowser import RoboBrowser

def get_list():
	my_url='https://yts.am/'

	browser=RoboBrowser(history=True,parser='html.parser')
	browser.open(my_url)

	containers=browser.find_all('div',attrs={'class':'browse-movie-wrap col-xs-10 col-sm-5'})
	count=1
	name=set([""])
	for container in containers:
		if(count==12): break
		name_container=container.find('div',attrs={'class':'browse-movie-bottom'})
		movie_name=name_container.text.strip()
		name.add(movie_name.replace('\n',' '))
		#print('NAME :'+name)
		count+=1
	return name


