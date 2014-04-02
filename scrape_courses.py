from selenium import webdriver
import credentials
from listings import listings
from bs4 import BeautifulSoup

 
browser = webdriver.Firefox()
browser.get('https://www-s.dmi.illinois.edu/course/crscrssearch.asp')

user_id_field = browser.find_element_by_id('UserID')
password_field = browser.find_element_by_id('Password')

user_id_field.send_keys(credentials.my_netid)
password_field.send_keys(credentials.my_password)


button = browser.find_element_by_name('BTN_LOGIN')
button.click()

# at this point, you should be logged in!


#here are the functions
#this guy grabs the table and writes it out to a csv
def grab_data(source):
	#bootyfulsoups goes here
	#writes out
	soup = BeautifulSoup(source)
	print(soup.prettify())
	pass


def process_option(i, el):
	#this chooses the first element only
	#button = browser.find_element_by_name('rptchoice')
	#but we want the button labeled "Detail"
	button = browser.find_elements_by_name('rptchoice')[1]

	el = browser.find_element_by_name('crschoice2')
	el = el.find_elements_by_tag_name('option')
	el[i].click()
	button.click()
	html_source = browser.page_source
	grab_data(html_source)
	browser.back() # and go back!


for l in listings:
	course_field = browser.find_element_by_name('rubrchoice')
	course_field.clear()
	course_field.send_keys(l)
	button = browser.find_element_by_name('rptchoice')
	button.click()

	button = browser.find_element_by_name('rptchoice')
	el = browser.find_element_by_name('crschoice2')
	el = el.find_elements_by_tag_name('option')
	for i in range(len(el)):
		process_option(i, el)

	browser.back() 	#go back again so we can input a new listing!


''' here is a snippet of my first attempt at traversing the options, preserved for posterity
for option in el.find_elements_by_tag_name('option'):
	el = browser.find_element_by_name('crschoice2')
	option.click()
	button.click()
	browser.back()
this method does not work, because of the way selenium works. we can look more into this later.
'''




