import itertools
import string
import time, pyautogui, clipboard
import bs4
import re

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

web = 'https://www.newegg.com/Desktop-Internal-Hard-Drives/SubCategory/ID-14?Tid=167523'

uClient = uReq(web) #start connection/based on url

page_html = uClient.read() #put content in here
uClient.close() #end connection


page_soup = soup(page_html, "html.parser")


containers = page_soup.findAll("div",{"class":"item-container"})

# print(containers[0])
print(len(containers))

#container = containers[0]

filename = "HDD_Newegg.csv"
f = open(filename, "w")

headers = "brand, product_name, shipping, price\n"

f.write(headers)

for container in containers:

	brand = (container.div.div.a.img["title"])
	title_container = container.findAll("a", { "class":"item-title" })
	product_name = title_container[0].text
	shipping_container = container.findAll("li", {"class":"price-ship"})
	shipping = shipping_container[0].text.strip()
	shipping = shipping_container[0].text.strip('')
	price_container = container.findAll("li", {"class":"price-current"})
	price = price_container[0].text.strip()
	
	#sub = re.sub("\D", "", price)
	strip = price.strip("$")



	print("Brand:  " + brand)
	print("Product Name  " + product_name)
	print("Shipping Rate  " + shipping)
	print("Price  " + strip)
	f.write(brand + "," + product_name.replace(",", "|") + "," + shipping + "," + "\n")

f.close()
# with open("Output.txt", "w") as text_file:
#	print (containers, file=text_file)


	# C:\Users\The Thor\AppData\Local\GitHubDesktop\bin
	# python -m pip install bs4


#title_container = container.findAll("a", {"class":"item-title"})
# print(container.div.div.a.img["title"])