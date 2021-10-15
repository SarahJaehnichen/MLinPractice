# Documentation of Data Science Tweets Classification for MLinpractice

October 10 2021

## Preprocessing 

### Punctuation Removal 

Given from point of depature:
* removes all punctuation given by string.punctuation 

Changes: 
* replaces special character '%' with the word 'percentage' in order to not lose the semantic information 
* only keeps alpha-numeric characters in a tweet, i.e. all special characters, punctuation and emojis are deleted - this makes further processing a lot easier. 

Possible addition/to do:
* replace all numeric characters with \<NUM\> token - with this we keep the information that the tweet contained a number without having to deal with specific numbers 
  

## Feature Extraction 

### Keywords/Content words

We use the rake-nltk package to extract keywords from the tweets. 
To DO: debug and finish feature extraction (counting of keywords for each tweet) 
