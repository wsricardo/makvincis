import urllib.request as request
from bs4 import BeautifulSoup

# Code for get web page like Web browser.

# Using base library network ("urllib")
# Blog: wsricardo.blogspot.com

# Web address
#url = "https://en.wikipedia.org/wiki/Main_Page"

# Open url and read web data
#data= request.urlopen(url).read()
#soup = BeautifulSoup(data.decode("utf8"), "html.parser")

data = ""

with open("data.html","r") as fl:
    data = fl.read()

#print(data.decode("utf8"))
soup = BeautifulSoup(data, "html.parser")
# Search tag with "id" mp-tfa in html code from web page.
art = soup.find_all(id="mp-tfa")

# Article text in html file search
for i in art:
    print(i.text)
