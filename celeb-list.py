#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests
from bs4 import BeautifulSoup

# Celebrity List URL, sorted by name
# (append this ->)  ?p=i&o=3
celebListUrl = "https://superkts.com/people/list/"


# redirect target url to next page (10 people per page)
def url(page):
    newUrl = []
    newUrl.append(celebListUrl)
    newUrl.append('?p=')
    newUrl.append(str(page))
    newUrl.append('&o=3')
    newUrl = ''.join(newUrl)
    
    return newUrl


# CRAWLING part
# Info: id / Name / Category / Age
member = []
print('---Starting Crawling---')

for p in range(247):
    webpage = requests.get(url(p+1))
    soup = BeautifulSoup(webpage.content, "html.parser")

    members = soup.find_all('td')
    members_list = members[:]

    #member = []
    
    for i in range(0, len(members_list), 6):
        key = soup.select('td')[i].text
        name = soup.select('td')[i+1].text
        category = soup.select('td')[i+2].text
        age = soup.select('td')[i+4].text
    
        packing = [key, name, category, age]
        member.append(packing)
    
print('---Celeb List Crawling finished---')


# result cvs: convert the dataFrame of clelbs
df = pd.DataFrame(member, columns=['ID', 'Name', 'Category', "Age"])

# REUSULT FILE: transfer to csv file
# file name: celeb_name_lis.cvs
df.to_csv('celeb_name_list.csv', index=False, encoding='utf-8-sig')
print('...Saved to csv file')


# In[114]:





# In[ ]:





# In[ ]:




