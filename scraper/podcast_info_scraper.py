#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 20:42:34 2021

@author: wengliangchong
"""

from bs4 import BeautifulSoup
import requests
import json
import pandas as pd

def to_int(value):
    if 'K' in value:
        return(int(float(value.replace('K', ''))*1000))
    elif 'M' in value:
        return(int(float(value.replace('M', ''))*1000000))
    elif 'B' in value:
        return(int(float(value.replace('B', ''))*1000000000))
    else:
        return(int(value))

def scrape(link):
    try:
        page = requests.get(link, timeout=20)
        soup = BeautifulSoup(page.content, "lxml")
        try:
            title = soup.find('h1').find('span').text.strip()
        except Exception:
            print("Missing title: ", link)
            title = ""
        try:
            producer = soup.find('h1').find('a').text.strip()
        except Exception:
            try:
                producer = soup.find('h1').find('span', class_='product-header__identity podcast-header__identity').text.strip()
            except Exception:
                print("Missing producder: ", link)
                producer = ""
        try:
            genre = soup.find('li', class_='inline-list__item inline-list__item--bulleted').text.strip()
        except Exception:
            print("Missing genre: ", link)
            genre = ""
        try:
            rating = float(soup.find('span', class_="we-customer-ratings__averages__display").text.strip())
        except Exception:
            print("Missing rating: ", link)
            rating = 0.0
        try:
            num_ratings = to_int(soup.find('div', class_="we-customer-ratings__count small-hide medium-show").text.strip().strip('Ratings'))
        except Exception:
            print("Missing number of ratings: ", link)
            num_ratings = 0
        try:
            num_episodes = int(soup.find('div', class_="product-artwork__caption small-hide medium-show").text.strip().strip('episodes').replace(',', ''))
        except Exception:
            print("Missing number of episodes: ", link)
            num_episodes = 0
        try:
            description = soup.find('div', class_="product-hero-desc product-hero-desc--spacer-bottom-large product-hero-desc--side-bar").text.strip()
        except Exception:
            print("Missing description: ", link)
            description = ""
    except Exception:
        print("Link not working:", link)
    details = {
        'title': title,
        'producer': producer,
        'genre': genre,
        'rating': rating,
        'num_ratings': num_ratings,
        'num_episodes': num_episodes,
        'description': description
        }
    return details

podcasts_dict = []
counter = 1

"""
with open('all_podcast_links.json') as file:
    links = json.load(file)
    for link in links:
        try:
            podcast_info = scrape(link)
            podcast_info['link'] = link
            podcasts_dict.append(podcast_info)
            if counter % 50 == 0:
                print(counter, 'podcasts done.')
            counter += 1
        except Exception:
            print(link, 'failed.')
            counter += 1
            pass

with open('./data/json/podcast_info.json', 'w') as outfile:
    json.dump(podcasts_dict, outfile)
"""

with open('../data/json/podcast_info.json') as file:
        podcasts = json.load(file)

df = pd.DataFrame(podcasts)
missing_df = df[df['title'].values == '']

for index, row in missing_df.iterrows():
    try:
        podcast_info = scrape(row.link)
        podcast_info['link'] = row.link
        podcasts_dict.append(podcast_info)
        print(counter, 'podcasts done.')
        counter += 1
    except Exception:
        print(row.link, 'failed.')
        counter += 1
        pass

with open('../data/json/podcast_info_add.json', 'w') as outfile:
    json.dump(podcasts_dict, outfile)

