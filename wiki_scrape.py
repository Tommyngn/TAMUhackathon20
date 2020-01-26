import requests
from bs4 import BeautifulSoup as BS

def scrape_url(url):

    response=requests.get(url)

    soup=BS(response.content,'lxml')

    table=soup.find_all('p')

    for i in table:
        print(i)