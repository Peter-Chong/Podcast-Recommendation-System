#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 20:03:25 2021

@author: wengliangchong
"""

import json
import requests
import pandas as pd
from bs4 import BeautifulSoup

"""
df = pd.read_pickle('../data/pickle/podcasts.pkl')
"""

with open('../data/json/podcast_eps.json') as file:
        df = pd.DataFrame(json.load(file))
titles = list(df.loc[df.episodes.str.len() == 0].title)
df = pd.read_pickle('../data/pickle/podcasts.pkl')
df = df.loc[df['title'].isin(titles)]

links = list(df.link)
titles = list(df.title)

podcast_dict = []
counter = 1

def scrape(link, title):
    epi = ""
    try:
        page = requests.get(link, timeout=20)
        soup = BeautifulSoup(page.content, "lxml")
        all_eps = soup.find_all('div', class_='we-truncate we-truncate--multi-line tracks__track__copy')
        for i in all_eps:
            epi = epi + " " + i.text.strip()
    except Exception:
        print("Link not working:", link)
    details = {
        'title': title,
        'episodes': epi
        }
    return details   

for link, title in zip(links, titles):
    try:
        podcast_info = scrape(link, title)
        podcast_dict.append(podcast_info)
        if counter % 50==0:
            print(counter, 'podcasts done.')
        counter += 1
    except Exception:
        print(link, 'failed.')
        counter += 1
        pass

with open('../data/json/podcast_eps_add.json', 'w') as outfile:
    json.dump(podcast_dict, outfile)