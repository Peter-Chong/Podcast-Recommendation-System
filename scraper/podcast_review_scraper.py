#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 18:10:38 2021

@author: wengliangchong
"""

import json
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

#df = pd.read_pickle('../data/pickle/podcasts.pkl')

with open('../data/json/podcast_reviews.json') as file:
        df = pd.DataFrame(json.load(file))
titles = list(df.loc[df.reviews.str.len() == 0].title)
df = pd.read_pickle('../data/pickle/podcasts.pkl')
df = df.loc[df['title'].isin(titles)]

links = list(df.link)
titles = list(df.title)

sublink = '#see-all/reviews'
podcast_dict = []
counter = 1

def scrape(link, title):
    reviews = ""
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(executable_path="../chromedriver", options=options)
        driver.get(link)
        time.sleep(1)
        page = driver.page_source
        soup = BeautifulSoup(page, "lxml")
        all_reviews = soup.find_all('div', class_='we-clamp')
        for i in all_reviews:
            reviews = reviews + " " + i.text.strip()
    except Exception:
        print("Link not working:", link)
    details = {
        'title': title,
        'reviews': reviews
        }
    return details

for link, title in zip(links, titles):
    full_link = link + sublink
    try:
        podcast_info = scrape(full_link, title)
        podcast_dict.append(podcast_info)
        if counter % 50==0:
            print(counter, 'podcasts done.')
        counter += 1
    except Exception:
        print(link, 'failed.')
        counter += 1
        pass

with open('../data/json/podcast_reviews_add.json', 'w') as outfile:
    json.dump(podcast_dict, outfile)