#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lemmatize the tokenized tweet such that words are given in their meaningful base form.

Created on Sun Oct 10 14:33:16 2021

@author: breise
"""

from code.preprocessing.preprocessor import Preprocessor
from nltk.stem.wordnet import WordNetLemmatizer
import ast

class Lemmatizer(Preprocessor):
    """Lemmatizes the given tokenized input column into base form words."""
    
    def __init__(self, input_column, output_column):
        """Initialize the Lemmatizer with the given input and output column.
        
        Input: must be tokenized already
        
        """
        super().__init__([input_column], output_column)
    
    # don't need to implement _set_variables(), since no variables to set
    
    def _get_values(self, inputs):
        """
        Lemmatize the tweet. 
        
        To Do:
            Debug - runtime error 
            Currently only default 'noun' considered- Add verbs.    
        
        """
        # initialze lemmatizer
        wnl = WordNetLemmatizer()
        
        lemmatized = []
        
        for tweet in inputs[0]:
            # tweets are strings, to get list of strings we can iterate through we use ast.literal_eval
            #tweet = ast.literal_eval(tweet)
            lemmatized_tweet = []
            # iterate through words of the tweet
            for word in tweet:
                # get lemma of word and add to list
                lemmatized_tweet.append(wnl.lemmatize(word))
                
            lemmatized.append(lemmatized_tweet)
        
        #lemmatized = [wnl.lemmatize(word) for tweet in inputs[0] for word in tweet]
        return lemmatized