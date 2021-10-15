#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Get the stem of words

Created on Sun Oct 10 16:40:33 2021

@author: breise
"""

from code.preprocessing.preprocessor import Preprocessor
from nltk.stem.snowball import SnowballStemmer
import ast

class Stemmer(Preprocessor):
    """Lemmatizes the given tokenized input column into base form words."""
    
    def __init__(self, input_column, output_column):
        """Initialize the Stemmer with the given input and output column.
        
        Input: must be tokenized already
        
        """
        super().__init__([input_column], output_column)
    
    # don't need to implement _set_variables(), since no variables to set
    
    def _get_values(self, inputs):
        """
        Stem the tweet. 
    
        """
        # initialize the stemmer
        sst = SnowballStemmer("english")
        
        stemmed = []
        
        # iterate through all tweets
        for tweet in inputs[0]:
            # tweets are strings, to get list of strings we can iterate through we use ast.literal_eval
            #tweet = ast.literal_eval(tweet)
            stemmed_tweet = []
            # iterate through words of the tweet
            for word in tweet:
                # get stem of word and add to list
                stemmed_tweet.append(sst.stem(str(word)))
                
            stemmed.append(stemmed_tweet)
        
        return stemmed