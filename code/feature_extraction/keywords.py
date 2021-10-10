#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 13:29:38 2021

@author: breise
"""

from rake_nltk import Rake
from code.feature_extraction.feature_extractor import FeatureExtractor

# class for checking tweets for keywords
class Keywords(FeatureExtractor):
    
    # constructor
    def __init__(self, input_column):
        super().__init__([input_column], "{0}_keywords".format(input_column))
    
    # don't need to fit, so don't overwrite _set_variables()
    
    # get all tweets and extract keywords from them, check how many of these keywords each tweet has (numeric feature)
    def _get_values(self, inputs):
        '''
        first get keywords from overall text, then calculate how many keywords a tweet has
        
        To DO:
            overall_text and keyword extraction currently not working 
            add counter for keywords 
        
        '''

        
    
        overall_text = ""
        for tweet in inputs[0]:
            overall_text += tweet
        
        r = Rake()
        r.extract_keywords_from_sentences(overall_text)
        keywords = r.get_ranked_phrases()
        
        # to do 
        # counter for how many keywords a tweet has
        # output: column with numeric feature 