import requests
from bs4 import BeautifulSoup as BS
from wiki_scrape import scrape_url

url='https://en.wikipedia.org/w/index.php?search=bushfires+2020&title=Special%3ASearch&go=Go&ns0=1'

combine='http://en.wikipedia.org'

response=requests.get(url)

soup=BS(response.content,'lxml')

# print(response.status_code)

table=soup.find_all('div',{'class': 'mw-search-result-heading'})

date=soup.find_all('div',{'class': 'mw-search-result-data'})

summary=soup.find_all('div',{'class': 'searchresult'})

list_of_urls=[]
list_of_titles=[]
list_of_summaries=[]
list_of_dates=[]

for i in table:
    list1=str(i).split('href="')
    list2=list1[1].split(' ')
    url_link=combine+(list2[0].rstrip('"'))
    list_of_urls.append(url_link)
    # print(url_link)

    listing=str(i).split('title="')
    listing2=listing[1].split('">')
    title=listing2[0]
    list_of_titles.append(title)
    # print(title)
    # print(i)

for i in summary:
    x=str(i)
    new_=x.replace('<span class="searchmatch">', '').replace('</span>','').split('">')
    info=new_[1].replace('</div>','')
    print(info)


# count=0
# for pos1, i in enumerate(date):
#     # print(i,' ASASASASAS')
#
#     list_=str(i).split(' - ')
#     list2=list_[1].split(',')
#     list3=list2[1].split('<')
#     list4=list3[0].split(' ')
#     month=list4[2]
#     date=list4[1]
#     year=list4[3]
#     #
#     print(list_of_urls[count])
#     print(month,date,year)
#     if pos1 == 0:
#         scrape_url(list_of_urls[count])
#     count+=1
#     break

