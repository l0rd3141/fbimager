#Facebook Image downloader

from bs4 import BeautifulSoup
import requests
import os,sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#Parse user input value
#uip = ''.join(sys.argv[1:])
uip=raw_input("Enter the number of photos you wish to download: ")

uip = int(uip)

email_addr = raw_input("Enter your facebook email: ")
password = raw_input("Enter your password: ")
friend_id = raw_input("Profile id of your friend: ")
directoryname = raw_input("Directory name: ")
if (not(os.path.exists("/home/"+directoryname))):
    os.mkdir(directoryname)
else:
    print(directory_name+" already exists, rename it or delete it")
#Downloads the image after getting the scontent link
def imageDownloader(url,filename):
	image = requests.get(url)
	imager = open(directoryname+'/'+filename,'wb')
	for data in image.iter_content(100000):
		imager.write(data)
	print("Downloaded" + str(x) + " image")

#Generates photolink
def photoLinkGenerator(source_file):
	photoLinkList = []
	#html_handler = open(html_file,'r')
	soup = BeautifulSoup(source_file)
	for values in soup.findAll('a',class_='uiMediaThumb _6i9 uiMediaThumbMedium'):
	    photoLinkList.append(values.get('href'))
	return photoLinkList


def scontentLinkGenerator((driverman,html_file)):
    photoLinkList = photoLinkGenerator(html_file)
    scontentLinkList = []
    driver = driverman
    for x in range(uip):
        driver.get(photoLinkList[x])
       #driver.save_screenshot("image"+str(x))
        sip = BeautifulSoup(driver.page_source)
        for values in sip.findAll('img',class_ = 'spotlight'):
            scontentLinkList.append(values.get('src'))
    return scontentLinkList
def seleniumWebPage(username,password,userid):
    driver = webdriver.Firefox()
    driver.get("https://facebook.com")
    email = driver.find_element_by_id("email")
    email.send_keys(username)
    passwd = driver.find_element_by_id("pass")
    passwd.send_keys(password)
    passwd.send_keys(Keys.RETURN)
    time.sleep(5)
    driver.get("https://facebook.com/"+userid+"/photos")
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(5)
    lel = driver.page_source
    driversource = (driver,lel)
    return driversource

linkmaster = scontentLinkGenerator(seleniumWebPage(email_addr,passwd,friend_id))

x = 0
for values in linkmaster:
    x=x+1
    #print values
    imageDownloader(values,str(4*x))
