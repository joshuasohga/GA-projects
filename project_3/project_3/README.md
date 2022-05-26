# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 3: Web APIs & NLP


# Problem Statement

Being part of an in-house Data Science Marketing Team of a beverage company venturing into e-commerce, my team and I are planning to leverage on Machine Learning to refine our recommendations to our e-customers, based on keywords.

The main objective of this project is to scrape two subreddits: <a href="https://reddit.com/r/coffee">r/coffee</a> and <a href="https://reddit.com/r/tea">r/tea</a> through a webscrapper, leveraging on Reddit's Pushshift API. The scraped data from the two subreddits will then be passed through various classification models, CountVectorizer/TfidVectorizer with Naive Bayes Classifier, LogisticRegression that will assign each observation to the most likely class of subreddit. The models should help the data science marketing team of my company identify what keywords are likely to predict the correct subreddit, and in turn, tailor a more enriching experience to our customers.

In this process, the subreddit posts will undergo preprocessing and EDA. The success of the models that we decide on will be determined through the highest accuracy based on the scores obtained.

---

## Executive Summary

There are no shortage of coffee or tea lovers in the world; millions, if not billions of people around the world begin their day with a cup of either beverages. According to a report published by ResearchAndMarkets, the "global ready to drink tea and coffee market has reached US$14 billion in 2020. Looking forward, the publisher expects the market to grow at a CAGR (compound annual growth rate) of 7.5% during 2021-2026. (<a href="https://www.researchandmarkets.com/reports/5353400/ready-to-drink-tea-and-coffee-market-global?utm_source=CI&utm_medium=PressRelease&utm_code=wgsm5l&utm_campaign=1621568+-+Global+Ready+to+Drink+Tea+and+Coffee+Market+(2021+to+2026)+-+Industry+Trends%2c+Share%2c+Size%2c+Growth%2c+Opportunity+and+Forecasts&utm_exec=jamu273prd">Source</a>)" Expectations may fall short, but this market is bound for growth.
 
In this project, my team seeks to explore the similarities and differences in keywords used between subreddits Coffee and Tea through its discussions and topics within their own respective communities. As a social news aggregation, web content rating and discussion website boasting over 52 million <b>daily active users</b> (<a href="https://backlinko.com/reddit-users">Source</a>), there is no other platform more suitable than Reddit to conduct our analysis. We believe that Reddit will be an insightful source of data to understand what are the popular topics in these respective subreddits.

To ease on code execution times, the web scraping portion will be done in a separate notebook. In the notebook labelled Project 3 - Final, I will be covering the steps taken to clean and analyze the data retrieved, steps taken to pre-process the text data, visualize the data and use different models to find the optimal model.

---

### Explanatory Data Analysis

Word Cloud - Most Common Words in Coffee and Tea subreddits

<img src="https://github.com/wrex303/GA-projects/blob/main/project_3/project_3/coffeewc.JPG?raw=true">
<br>
<br>
<br>


<img src="https://github.com/wrex303/GA-projects/blob/main/project_3/project_3/teawc.JPG?raw=true">


---

## Summary of Results/Conclusion

|Model|Vectorizer|Training Score|Testing Score|TN|FN|TP|FP|Delta|
|---|---|---|---|---|---|---|---|---|
|Naive-Bayes|Count Vectorizer|0.926|0.860|392|62|330|56|0.066|
|Naive-Bayes|TFIDF Vectorizer|0.963|0.865|419|84|308|29|0.098|
|Logistics Regression|Count Vectorizer|0.972|0.844|373|56|336|75|0.128|
|Logistics Regression|TFIDF Vectorizer|0.956|0.839|389|76|316|59|0.117|

After running our data through 4 model combinations, I have chosen the `MultinomialNB - CvecVectorizer model` combination with a score of 86.0% in predicting which subreddit a post came from (Coffee or Tea). Although the model came in second in test score, the basis for choosing this model was due to the lower delta between the Train and Test score (0.066) as compared to the higher delta between the model with the highest test score (0.098). Moreover, this model also had a high ROC-AUC score of <b>95.2%</b> - meaning the model is able to mostly distinguish between the positive and negative classes.

Using GridSearchCV, the best hyperparameters for this particular model is:
* 'cvec__max_df': 0.6,
* 'cvec__max_features': 2000,
* 'cvec__min_df': 2,
* 'cvec__ngram_range': (1, 1),
* 'nb__alpha': 0.25

From our Data Visualizations, we have identified Coffee Subreddit to have key words such as `grinder`, `grind`, `burr`, `roaster`. On the other hand, the Tea subreddit tends to have key words like `oolong`, `pu`, `er`, and `gaiwan`. Given enough time, perhaps a further study can be conducted to understand how and why words such as `grind` and `burr` are some of the top keywords for the Coffee subreddit.

---

## Recommendations

When it comes to modelling, introducing more data features may improve our modelling accuracy scores. One other possible area of focus can be the comments section of subreddit threads. 

Since Reddit also has numerous submissions where the selftext is an image (imgur.com), if these can be used in Machine Learning for image classification, it may also help to improve our accuracy scores.

---
## Data Dictionary
---
| Parameter | Description |
| ------ | ------ |
| is_robot_indexable | Used to determine if a post has been deleted - if TRUE, the post still exists. If FALSE, the post can not be found on the subreddit. Main parameter for dropping deleted posts |
| size | Number of posts to pull (capped at 100 per instance) |
| subreddit | Restrict to a specific subreddit (r/coffee and r/tea) |
| selftext  | Body text of the post |
| title | Title of the post |
| string_count | Number of strings for each post |
| word_count | Number of words for each post |
| text | A corpus of pre-processed text following cleaning, tokenization, lemmatization and removal of stopwords |
