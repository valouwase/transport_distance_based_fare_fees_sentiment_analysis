#!/usr/bin/env python
# coding: utf-8

# # Sentiment Analysis of Distance-Based Fare Policy in Rwanda
# This notebook presents the data extraction of public feedback regarding Rwanda’s shift to a distance-based fare pricing model. The analysis draws on user comments from Twitter/X and YouTube using Google Cloud NLP.

# ### Installing libraries and importing them to help me retrieve data from social media

# In[1]:


pip install youtube-comment-downloader


# In[2]:


get_ipython().system('pip install snscrape')


# In[6]:


get_ipython().system('pip install google-api-python-client')


# ## 1. Data collection

# In[10]:


import googleapiclient.discovery
import googleapiclient.errors

api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = "AIzaSyAZy52kyQq-dm8FXorr5oCB_T2NwGvQgSc"
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=DEVELOPER_KEY)

request = youtube.commentThreads().list(
    part="snippet",
    videoId="wBUBEVRMn98",
    maxResults=100
)
response = request.execute()

for item in response['items']:
    print(item['snippet']['topLevelComment']['snippet']['textDisplay'])


# In[11]:


api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = "AIzaSyAZy52kyQq-dm8FXorr5oCB_T2NwGvQgSc"
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=DEVELOPER_KEY)

request = youtube.commentThreads().list(
    part="snippet",
    videoId="g4HB-VPFMQc",
    maxResults=100
)
response = request.execute()

for item in response['items']:
    print(item['snippet']['topLevelComment']['snippet']['textDisplay'])


# ### Trying to scrape data from X (Twitter)

# In[4]:


import snscrape.modules.twitter as sntwitter
#import pandas as pd

# Define your search query
query = "rwanda fare OR RURA OR public transport OR distance-based fare since:2024-01-01 until:2025-05-16"
query = "Rwanda transport"

# Collect tweets
tweets = []
for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
    if i > 50:  # Limit to 50 tweets for now
        break
    tweets.append([tweet.date, tweet.user.username, tweet.content])

# Save to DataFrame
df = pd.DataFrame(tweets, columns=["Date", "User", "Tweet"])
df.to_csv("tweets.csv", index=False)

# Show first few rows
df.head()


# In[ ]:


import snscrape.modules.twitter as sntwitter
#import pandas as pd

username = "oswaki"
tweet_id = "1916894908868104335"
query = f"to:{username} since:2024-01-01"

replies = []

for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
    if hasattr(tweet, 'inReplyToTweetId') and tweet.inReplyToTweetId == int(tweet_id):
        replies.append([tweet.date, tweet.user.username, tweet.content])
    if i >= 100:  # limit to 100 replies
        break

df = pd.DataFrame(replies, columns=["Date", "User", "Reply"])
df.to_csv("replies_to_oswaki.csv", index=False)
df.head()


# ### Challenges encountered 
# After trying to scrape data from Twitter I got an error since tweets were blocked I tried another method of screenshooting the tweets and entering manually in a dataset. 

# In[18]:





# In[ ]:




