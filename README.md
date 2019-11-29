# sentiment-analysis
The underlying question of this project is interesting: can we use our knowledge of the sentiment analysis of regular tweet to 
do online election polling and predict results of elections?

## What we'll do:
The tweets are raw. They are web-scraped straight from the internet. Amongst the python libraries we'll use to clean and process the text is
NLTK, re and BeautifulSoup. We'll have a look at the data and then use a few vectorizers to the numerically process the data for us to be able to build
ML models which can train on this vectorized data. 
We'll then test a few machine learning algorithms. A lot of them actually. We'll see how we can tune them for better performance, and pick the 
best one to check our underlying question. (The answer is interstingly: It did really well, but it can be better. Btw)

**Tip of the mountain:** We compare the prediction of the model to the actual results of the 2019 Canadian Federal elections in the end.

## What you'll need:
All the data files are in the zip.

## Libraries that we'll be using:
1) Cleaning: NLTK, re, BeautifulSoup
2) ML models: Sklearn's Logistic Regression, Naive Bayes, AdaBoost, XGBoost, Random Forests, Linear SVM, and Neural Nets.

## To whom this is targetted
Students who want to learn the basics of processing test data and build their first Natural Language Processing/sentiment analysis model.
I focus much on the preliminary data analysis so that you get a feel of what goes in a data science project before any of the code is written
