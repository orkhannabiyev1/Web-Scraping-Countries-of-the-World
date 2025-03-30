
import requests
from bs4 import BeautifulSoup
url = "https://www.scrapethissite.com/pages/simple/"
response=requests.get(url)
soup=BeautifulSoup(response.text,"html.parser")
mpm=soup.find('section',{'id':'countries'})
cont=mpm.find('div',{'class':'container'})
rows=cont.find_all('div',{'class':'row'})
for row in rows:
    countries = row.find_all('div', {'class': 'col-md-4 country'})
    if len(countries)==3:
        for c in countries:
            name=c.find('h3', {'class': 'country-name'})
            lst=name.text.strip()
            print(lst)




