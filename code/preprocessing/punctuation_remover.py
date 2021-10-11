#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Preprocessor that removes punctuation and special characters from the original tweet text.

Created on Wed Sep 29 09:45:56 2021
Changed on Sat Oct 10 2021

@author: breise
"""


import re
from code.preprocessing.preprocessor import Preprocessor
from code.util import COLUMN_TWEET, COLUMN_PUNCTUATION


class PunctuationRemover(Preprocessor):
    
    # constructor
    def __init__(self):
        # input column "tweet", new output column
        super().__init__([COLUMN_TWEET], COLUMN_PUNCTUATION)
    
    
    # get preprocessed column based on data frame and internal variables
    def _get_values(self, inputs):
        # replace special character of percentage with the word (to not lose the semantic information here)
        column = [re.sub(r'\%', ' percent', tweet) for tweet in inputs[0]]
        # replace all characters and symbols that are not alpha-numeric with empty string
        # this eliminated all punctuation, special characters and emojis
        column = [re.sub(r'[^A-Za-z0-9\s]+', '', tweet) for tweet in column]
        # exchange numbers with <num> token - actual numbers might be uninteresting and this could make comparing/further preprocessing easier 
        column = [re.sub(r'[0-9]+$', '<NUM>', tweet) for tweet in column]
        
        return column