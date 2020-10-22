#!/usr/bin/env python
# coding: utf-8

# In[13]:


### Key, Access Token 추가###
import tweepy
import os


# API 인증요청
consumer_key = "naU4BhMQ3xFdSqm90pvn1xbHk"
consumer_secret = "17bgr8gQHmdrSUQlhJAF9yDB0TH7N2Jt0Z9NBlRa2wQmTvqUB1"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# access 토큰 요청
access_token = "1316714233610952704-FPQUodQxinE2koV0MMDOu0FjAypBlr"
access_token_secret = "Kc0zL3Pdc6JBvMdStP4XMjQkB6UyodSmiuDSk2JdgmunE"
auth.set_access_token(access_token, access_token_secret)

#twitter API 생성
api = tweepy.API(auth)


# In[14]:


### Twitter 검색 cursor 선언

location = "%s, %s, %s" % ("35.95", "128.25", "1000km")
keyword = "언더아머"

wfile = open(os.getcwd()+"/twitterCompImage.txt", mode ='w', encoding='UTF-8')

## since랑 count만 건들면 됩니당
cursor = tweepy.Cursor(api.search, 
                       q=keyword,
                      since ='2020-01-01',
                      count= 1000,
                      include_entities=True)


# In[15]:


for i, tweet in enumerate(cursor.items()):
    print("{}: {}".format(i, tweet.text))
    wfile.write(tweet.text+'\n')

print("===Twitter Crawling for Company Image is Complete===")
wfile.close()


# In[ ]:




