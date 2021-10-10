#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Get the stem of words

Created on Sun Oct 10 16:40:33 2021

@author: breise
"""

from code.preprocessing.preprocessor import Preprocessor
from nltk.stem.snowball import SnowballStemmer

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
        To DO:
            debug (creates column etc but no actual stemming happens)
        """
        sst = SnowballStemmer("english")
        stemmed = [sst.stem(tweet) for tweet in inputs[0]]
        #stemmed = [sst.stem(word) for tweet in inputs[0] for word in tweet]
        return stemmed