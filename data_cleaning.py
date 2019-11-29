import json
import numpy as np
import pandas as pd
import nltk
import matplotlib.pyplot as plt
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer 
from bs4 import BeautifulSoup
import re
import string

ps = nltk.PorterStemmer()
lemmatizer = WordNetLemmatizer()

f = open("stop_words.txt", "r")
stop_words = f.read().split('\n')

df = pd.read_csv('generic_tweets.txt')

#%%
def get_wordnet_pos(w):
    ''' input: word (string)
    output: part-of-speech of word
    '''
    pos = nltk.pos_tag([w])[0][1][0].upper()
    pos_dict = {"J": wordnet.ADJ,"N": wordnet.NOUN,"V": wordnet.VERB,"R": wordnet.ADV}
    return pos_dict.get(pos, wordnet.ADV)

def clean_tweet(s):
    '''
    '''    
    s = str.lower(BeautifulSoup(s).get_text()) # remove html tags and lower case
    s.replace('‘', "'").replace('’', "'").replace('“', "'").replace('”', "'") # replace any fancy apostrophes
    s = re.sub(r'@[A-Za-z0-9]+', '', s) # remove twitter handles '@...'
    s = re.sub('https?://[A-Za-z0-9./]+', '', s) # remove links
    s  = "".join([char for char in s if char not in '!"$%&#()*+,-./:;<=>?@[\\]^_`{|}~\n\t\v\b']) # remove punctuation 
    s = re.sub('[0-9]+', '', s) # remove numbers
    s = nltk.word_tokenize(s) # tokenize
    s = [w.replace('\'', '') for w in s] # remove remaining apostrophes
    s = [w for w in s if w not in stop_words]  # remove stop words
    s = [w for w in s if len(w)>2] # remove single and double character strings if any
    s = [lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in s] # porter stem words   
    s = ' '.join(s) # join words to make sentence again
    #s = ' '.join([w for w in s if w not in stop_words]) # an additional check for stop words
    
    return s

clean_text = [clean_tweet(s) for s in df.text]

