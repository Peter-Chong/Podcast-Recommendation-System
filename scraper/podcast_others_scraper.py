#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 21:23:22 2021

@author: wengliangchong
"""

import json
import requests
import pandas as pd
from bs4 import BeautifulSoup

df = pd.read_pickle('../data/pickle/podcasts.pkl')
links = list(df.link)
titles = list(df.title)

podcast_dict = []
counter = 1

def scrape(link, title):
    try:
        also_subs_to = []
        page = requests.get(link, timeout=20)
        soup = BeautifulSoup(page.content, "lxml")
        first_level = soup.find_all('div', class_='l-row l-row--peek')[2]
        second_level = first_level.find_all('div', class_='we-truncate we-truncate--single-line targeted-link__target')
        for i in second_level:
            also_subs_to.append(i.text.strip())
    except Exception:
        print("Link not working:", link)
        also_subs_to = []
    details = {
        'title': title,
        'also_subs_to': also_subs_to
        }
    return details

for link, title in zip(links, titles):
    try:
        podcast_info = scrape(link, title)
        podcast_dict.append(podcast_info)
        print(counter, 'podcasts done.')
        counter += 1
    except Exception:
        print(link, 'failed.')
        counter += 1
        pass

with open('../data/json/podcast_also_subs_to.json', 'w') as outfile:
    json.dump(podcast_dict, outfile)
