#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tokenize the tweet into individual words.

Created on Wed Oct  6 13:59:54 2021

@author: lbechberger
"""

from code.preprocessing.preprocessor import Preprocessor
from nltk.tokenize import TweetTokenizer

class Tokenizer(Preprocessor):
    """Tokenizes the given input column into individual words."""
    
    def __init__(self, input_column, output_column):
        """Initialize the Tokenizer with the given input and output column."""
        super().__init__([input_column], output_column)
    
    # don't need to implement _set_variables(), since no variables to set
    
    def _get_values(self, inputs):
        """Tokenize the tweet."""
        
        tokenizer = TweetTokenizer()
        
        tokenized = [tokenizer.tokenize(tweet) for tweet in inputs[0]]
        
        #for tweet in inputs[0]:
         #   tokenized_tweet = tokenizer.tokenize(tweet)
          #  tokenized.append(tokenized_tweet)
        
        return tokenized