# Documentation of Data Science Tweets Classification for MLinpractice

October 10 2021

## Preprocessing

### Lemmatizer

Lemmatization can be a useful pre-processing step to get the meaningful base form of words for easier semantic comparison. Here we use WordNet as a knowledge base for finding the base forms (nltk WordNetLemmatizer)
Drawback: WordNet does not always capture the correct meaning of a word and is computationally expensive

To Do: debug and add verbs (currently only nouns considered)

### Stemming

Stemming is useful to get the stem of a word and get rid of pre- and suffixes; this too makes comparison between tweets easier.

To Do: debug 
