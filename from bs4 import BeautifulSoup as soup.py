from bs4 import BeautifulSoup as soup
from urllib.request import urlopen


#site parameters
site = "https://www.espncricinfo.com/sitemap.xml"

# open the site
op = urlopen(site)

#read the data
rd = op.read()

#close the object
op.close()

#scrape the data
sp_page = soup(rd, 'xml')
print(sp_page)


matchlist = sp_page.find_all('description')