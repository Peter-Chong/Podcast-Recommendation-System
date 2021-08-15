# Podcast Recommendation System
  
<img src="https://github.com/Peter-Chong/Podcast-Recommendation-System/blob/main/images/podcast-recs-blog-header-815x380.png" width="900" height="230" />

## Problem Statement

As an avid podcast listener, I always listen to them while I am doing my house chores. However, I find myself spending more time browsing for a good podcast than doing my house chores. This got me thinking, why don't I create a podcast recommender to recommend me a podcast rather than choosing based on the titles?

## Project Overview

* Built a web scrapper from scratch and scraped 4,460 podcasts data from Apple Podcast using Selenium and BeautifulSoup  
* Cleaned data by removing non-English podcasts, URLs and non-alphanumeric characters using regular expressions  
* Showcased Natural Language Processing techniques by tokenizing texts, remove stop words and stem texts using lemmatization  
* Performed exploratory data analysis and created plots such as Network Graph to see the relationships between podcasts  
* Created 3 different models to transform texts into vector/matrix representation (Bag-of-Words, TF-IDF and Word2Vec)

## Exploratory Data Analysis


## Recommendation System


### Text Pre-Processing


### CountVectorizer (Bag-Of-Words) + Cosine Similarity


### TF-IDF + Cosine Similarity


### Word2Vec + Cosine Similarity


## Future Scope


## Code and Resources:  
**Programming Language:** Python  
**Packages:** NumPy, Pandas, NLTK, Plotly, Scikit-Learn, Gensim, json, re, UMAP, NetworkX, BeautifulSoup4, Selenium    
**Data Soucres:** https://podcasts.apple.com/us/genre/podcasts/id26  
**Resources:**  
https://www.ywcascotland.org/feminism-podcast-recommendations/  
https://github.com/siddgood/podcast-recommendation-engine
