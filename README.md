# Podcast Recommendation System
  
<img src="https://github.com/Peter-Chong/Podcast-Recommendation-System/blob/main/images/podcast-recs-blog-header-815x380.png" width="900" height="230" />

## Problem Statement

As an avid podcast listener, I always listen to one while I am doing my house chores. However, I often find myself spending more time browsing for a good podcast channel than actually listening to them. This got me thinking, why don't I create a podcast recommender to give me suggestions for a podcast rather than simply choosing based on the podcast's titles?

## Project Overview

* Built a web scraper from scratch and scraped 4,460 podcasts data from Apple Podcast using Selenium and BeautifulSoup  
* Cleaned data by removing non-English podcasts, URLs and non-alphanumeric characters using regular expressions  
* Showcased Natural Language Processing techniques by tokenizing texts, removing stop words and stemming texts using lemmatization  
* Performed exploratory data analysis and created plots such as Network Graph to see the relationships between podcasts  
* Created 3 different models to transform texts into vector/matrix representation (Bag-of-Words, TF-IDF and Word2Vec)

## [Exploratory Data Analysis](https://nbviewer.jupyter.org/github/Peter-Chong/Podcast-Recommendation-System/blob/main/notebook/Exploratory%20Data%20Analysis.ipynb)

One interesting analysis I did was I created a network graph. Given a podcast, the data I scraped would include what other subscribers of that podcast also subscribed to. The network graph then visualized those relationships. However, 4,460 podcasts are too many to be visualized in a 2-dimensional graph. Hence, we'll just look into one of the genres, namely the education genre.

<img src="https://github.com/Peter-Chong/Podcast-Recommendation-System/blob/main/images/map.png" />

Other than that, I have also created a word cloud plot for each genre. The bigger the word is, the more frequent it is used in the podcast's description. For example, gardening and game is two common words in the Leisure genre, life and expert in Health & Fitness genre and interview and musician in the Music genre.

<img src="https://github.com/Peter-Chong/Podcast-Recommendation-System/blob/main/images/leisure.png" />

<img src="https://github.com/Peter-Chong/Podcast-Recommendation-System/blob/main/images/health.png" />

<img src="https://github.com/Peter-Chong/Podcast-Recommendation-System/blob/main/images/music.png" />

## [Recommendation System](https://nbviewer.jupyter.org/github/Peter-Chong/Podcast-Recommendation-System/blob/main/notebook/Recommendation.ipynb)

### Text Pre-Processing

We first concatenate the textual columns and pre-process them by the following steps:
1. Remove any links (URLs)
2. Tokenize text
3. Remove custom stop words
4. Lemmatize text

### CountVectorizer (Bag-Of-Words) + Cosine Similarity

We then apply CountVectorizer model which utilizes bag-of-words method to count the frequency of words in the text. Then we use cosine similarity to recommend 5 other podcasts. The figure below shows some examples of recommendations.

<img src="https://github.com/Peter-Chong/Podcast-Recommendation-System/blob/main/images/bow_recs.png" />

If the recommendation is one of the podcasts the subscriber also subscribed to, it will mark as true positive. We can also see that the recommendation is fairly accurate as the 5 recommendations are all within the same genre as the input podcast.  
  
We then try to visualize the CountVectorizer matrix by applying supervised UMAP and reduce the dimension to 2. 

<img src="https://github.com/Peter-Chong/Podcast-Recommendation-System/blob/main/images/bow_umap.png" />

### TF-IDF + Cosine Similarity

Next, we then apply TF-IDF model to vectorize the text. This model works well since it reduces the weight for those frequent and generic words such as "podcast" or "this". As we can observe in the UMAP plot below, this model clusters the genre pretty well.

<img src="https://github.com/Peter-Chong/Podcast-Recommendation-System/blob/main/images/tfidf_recs.png" />

<img src="https://github.com/Peter-Chong/Podcast-Recommendation-System/blob/main/images/tfidf_umap.png" />

### Word2Vec + Cosine Similarity

Lastly, we apply the Word2Vec model. 

<img src="https://github.com/Peter-Chong/Podcast-Recommendation-System/blob/main/images/w2v_recs.png" />

The Word2Vec model comes with a function to see the "synonym" of a word. For example, the word funny is most similar to the word hilarious and delightfully based on our model.

<img src="https://github.com/Peter-Chong/Podcast-Recommendation-System/blob/main/images/w2v_top10.png" />

The UMAP also shows a nice clustering between the genres.

<img src="https://github.com/Peter-Chong/Podcast-Recommendation-System/blob/main/images/w2v_umap.png" />

## Future Scope

In the future, I hope to:
1) Apply different model such as GloVe
2) Recommend podcast episodes instead
3) Create a better testing metric such as genre classification to validate model
4) Try out collaborative filtering

## Code and Resources:  
**Programming Language:** Python  
**Packages:** NumPy, Pandas, NLTK, Plotly, Scikit-Learn, Gensim, json, re, UMAP, NetworkX, BeautifulSoup4, Selenium    
**Data Soucres:** https://podcasts.apple.com/us/genre/podcasts/id26  
**Resources:**  
https://www.ywcascotland.org/feminism-podcast-recommendations/  
https://github.com/siddgood/podcast-recommendation-engine
