#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Preprocessor that removes punctuation from the original tweet text.

Created on Wed Sep 29 09:45:56 2021

@author: lbechberger
"""

import string
from code.preprocessing.preprocessor import Preprocessor

# removes punctuation from the original tweet
# inspired by https://stackoverflow.com/a/45600350
class PunctuationRemover(Preprocessor):
    
    # constructor
    def __init__(self):
        # input column "tweet", new output column
        super().__init__(["tweet"], "tweet_no_punctuation")
    
    # set internal variables based on input columns
    def _set_variables(self, inputs):
        # store punctuation for later reference
        self._punctuation = "[{}]".format(string.punctuation)
    
    # get preprocessed column based on data frame and internal variables
    def _get_values(self, df):
        # replace punctuation with empty string
        column = df[self._input_columns[0]].str.replace(self._punctuation, "")
        return column