#!/usr/bin/env python
# coding: utf-8

# # question 01

# In[1]:


import requests
from bs4 import BeautifulSoup

# URL of the page to be scraped
url = "https://www.youtube.com/@PW-Foundation/videos"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the video links on the page
video_links = soup.find_all('a', {'class': 'yt-simple-endpoint style-scope ytd-grid-video-renderer'})

# Extract the video URLs of the first five videos
video_urls = []
for link in video_links[:5]:
    video_urls.append('https://www.youtube.com' + link['href'])

# Print the video URLs
print(video_urls)


# # question 02

# In[2]:


import requests
from bs4 import BeautifulSoup

# URL of the page to be scraped
url = "https://www.youtube.com/@PW-Foundation/videos"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the video links on the page
video_links = soup.find_all('a', {'class': 'yt-simple-endpoint style-scope ytd-grid-video-renderer'})

# Extract the thumbnail URLs of the first five videos
thumbnail_urls = []
for link in video_links[:5]:
    thumbnail = link.find('img')
    if thumbnail:
        thumbnail_urls.append(thumbnail['src'])

# Print the thumbnail URLs
print(thumbnail_urls)


# # question 03
https://www.youtube.com/@PW-Foundation/videos
Write a python program to extract the title of the first five videos.
# In[3]:


import requests
from bs4 import BeautifulSoup

# URL of the page to be scraped
url = "https://www.youtube.com/@PW-Foundation/videos"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the video links on the page
video_links = soup.find_all('a', {'class': 'yt-simple-endpoint style-scope ytd-grid-video-renderer'})

# Extract the titles of the first five videos
video_titles = []
for link in video_links[:5]:
    title = link.find('span', {'class': 'style-scope ytd-grid-video-renderer'})
    if title:
        video_titles.append(title.text)

# Print the video titles
print(video_titles)


# # question 04

# In[4]:


import requests
from bs4 import BeautifulSoup

# URL of the page to be scraped
url = "https://www.youtube.com/@PW-Foundation/videos"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the video links on the page
video_links = soup.find_all('a', {'class': 'yt-simple-endpoint style-scope ytd-grid-video-renderer'})

# Extract the number of views of the first five videos
video_views = []
for link in video_links[:5]:
    view_count = link.find('span', {'class': 'style-scope ytd-grid-video-renderer'})
    if view_count:
        video_views.append(view_count.text.strip())

# Print the number of views
print(video_views)


# # question 05 

# In[ ]:


import requests
from bs4 import BeautifulSoup

# URL of the page to be scraped
url = "https://www.youtube.com/@PW-Foundation/videos"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the video links on the page
video_links = soup.find_all('a', {'class': 'yt-simple-endpoint style-scope ytd-grid-video-renderer'})

# Extract the publication date of the first five videos
video_dates = []
for link in video_links[:5]:
    video_url = "https://www.youtube.com" + link['href']
    video_response = requests.get(video_url)
    video_soup = BeautifulSoup(video_response.content, 'html.parser')
    date = video_soup.find('div', {'id': 'date'})
    if date:
        video_dates.append(date.text.strip())

# Print the publication dates
print(video_dates)


# In[ ]:




