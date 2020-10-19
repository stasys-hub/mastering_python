
import bs4                                  # beautiful soup 
from urllib.request import urlopen as uReq  # open urls
from bs4 import BeautifulSoup as soup       # 

#setup url to webscrape -> graphics cards queery on newegg
my_url = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphic+cards"

#download the webpage
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")

#header
page_soup.findAll("div",{"





