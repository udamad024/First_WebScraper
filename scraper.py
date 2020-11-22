from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'http://www.newegg.com/Product/ProductList.aspx?Submit=ENE&N=-1&IsNodeId=1&Description=GTX&bop=And&Page=1&PageSize=36&order=BESTMATCH'

uClient = uReq(my_url) #opens connection to URL, grabbing the page
page_html = uClient.read() #Gets the HTML file from opened URL
uClient.close() #Closes Connection

#HTML parsing
page_soup = soup(page_html, "html.parser")

containers =  page_soup.findAll("div",{"class":"item-container"}) #context - all graphics cards are coded in a <d, /d>(which is basically a section), and have used the class container

len(containers) #basically the amount of graphic cards (more specifically the amount of containers) show in the html

filename = "products.csv"
f = open(filename, "w")

headers = "Brand, Product_name, shipping\n" #header in csv file (excel)
f.write(headers) # #first line is header

for container in containers:
  brand = container.div.div.a.img["title"] #Gets the title "MSI"

  title_container = container.findAll("a",{"class":"item-title"}) #gets the title from tag a, class item  title "MSI LAPTOP"
  product_name = title_container[0].text #As the titles is in a <a> but not another, its just put in text.

  shipping_container = container.findAll("li",{"class":"price-ship"})
  shipping = shipping_container[0].text
     

  print("Brand: " + brand)
  print("Product: " + product_name) 
  print("Shipping: " + shipping)

  
  f.write(brand + "," + product_name.replace(",","|") + "," + shipping + "\n")

f.close()
