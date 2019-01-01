from bs4 import BeautifulSoup
import urllib.request
import csv
import numpy
import pandas as pd

tags = []
titles = []
pageId = 1
for pageId in range(5000, 5100):
    print("id=", pageId)
    url = ("https://stackoverflow.com/questions/tagged/node.js?sort=newest&page={}&pagesize=20").format(pageId)
    print("url=", url)

    try:
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, 'lxml')
        for link in soup.find_all('a'):
            if (link.get('class') != None):
                list1 = link.get('class')
                for li in list1:
                    if li == "question-hyperlink":
                        print('li=', li)
                        titles.append(link.text)
                        tags.append(link.get('href'))
    except:
        pass
    
s1 = pd.Series(tags, name='list1')
s2 = pd.Series(titles, name='list2')
df = pd.concat([s1, s2], axis=1)
df.to_csv("tagsWithTitles11.csv")
