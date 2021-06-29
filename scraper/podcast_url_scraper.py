#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 19:21:38 2021

@author: wengliangchong
"""

from bs4 import BeautifulSoup
import requests
import json

base = "https://podcasts.apple.com/us/genre/"

query_param = {
    'arts': "podcasts-arts/id1301",
    'business': "podcasts-business/id1321",
    'comedy': "podcasts-comedy/id1303",
    'education': "podcasts-education/id1304",
    'fiction': "podcasts-fiction/id1483",
    'government': "podcasts-government/id1511",
    'health_and_fitness': "podcasts-health-fitness/id1512",
    'history': "podcasts-history/id1487",
    'kids_and_family': "podcasts-kids-family/id1305",
    'leisure': "podcasts-leisure/id1502",
    'music': "podcasts-music/id1310",
    'news': "podcasts-news/id1489",
    'religion_and_spirituality': "podcasts-religion-spirituality/id1314",
    'science': "podcasts-science/id1533",
    'society_and_culture': "podcasts-society-culture/id1324",
    'sports': "podcasts-sports/id1545",
    'tv_and_film': "podcasts-tv-film/id1309",
    'technology': "podcasts-technology/id1318",
    'true_crime': "podcasts-true-crime/id1488"
}

links = []

for url in query_param.values():
    full_url = base + url
    try:
        page = requests.get(full_url, timeout=3)
        soup = BeautifulSoup(page.content, "lxml")
        columns = soup.find('div', class_='grid3-column')
        for i in columns.findAll('a'):
            links.append(i.get('href'))
    except AttributeError:
        print(url, "caused an error.")

with open('all_podcast_links.json', 'w') as outfile:
    json.dump(links, outfile)