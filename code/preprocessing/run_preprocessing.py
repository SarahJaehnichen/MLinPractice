#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Runs the specified collection of preprocessing steps

Created on Tue Sep 28 16:43:18 2021

@author: lbechberger
"""

import argparse, csv, pickle
import pandas as pd
from sklearn.pipeline import make_pipeline
from code.preprocessing.punctuation_remover import PunctuationRemover
from code.preprocessing.tokenizer import Tokenizer
from code.preprocessing.lemmatizer import Lemmatizer
from code.preprocessing.stemmer import Stemmer
from code.util import COLUMN_TWEET, SUFFIX_TOKENIZED, TWEET_TOKENIZED, SUFFIX_LEMMATIZED, SUFFIX_STEMMED

# setting up CLI
parser = argparse.ArgumentParser(description = "Various preprocessing steps")
parser.add_argument("input_file", help = "path to the input csv file")
parser.add_argument("output_file", help = "path to the output csv file")
parser.add_argument("-dev", "--development", action= "store_true", help = "preprocess with less data to shorten runtime during development")
parser.add_argument("-p", "--punctuation", action = "store_true", help = "remove punctuation")
parser.add_argument("-t", "--tokenize", action = "store_true", help = "tokenize given column into individual words")
parser.add_argument("--tokenize_input", help = "input column to tokenize", default = COLUMN_TWEET)
parser.add_argument("-l", "--lemmatize", action = "store_true", help = "lemmatize given tokenized words into meaningful base forms")
parser.add_argument("--lemmatize_input", help = "input column to lemmatize", default = TWEET_TOKENIZED) 
parser.add_argument("-st", "--stemming", action = "store_true", help = "get stem of given tokenized words")
parser.add_argument("--stemming_input", help = "input column to stem", default = TWEET_TOKENIZED)
parser.add_argument("-e", "--export_file", help = "create a pipeline and export to the given location", default = None)
args = parser.parse_args()

# load data
df = pd.read_csv(args.input_file, quoting = csv.QUOTE_NONNUMERIC, lineterminator = "\n")
if args.development:
    df = df[:100]

# collect all preprocessors
preprocessors = []
if args.punctuation:
    preprocessors.append(PunctuationRemover())
if args.tokenize:
    preprocessors.append(Tokenizer(args.tokenize_input, args.tokenize_input + SUFFIX_TOKENIZED))
if args.lemmatize:
    preprocessors.append(Lemmatizer(args.lemmatize_input, args.lemmatize_input + SUFFIX_LEMMATIZED))
if args.stemming:
    preprocessors.append(Stemmer(args.stemming_input, args.stemming_input+ SUFFIX_STEMMED))

# call all preprocessing steps
for preprocessor in preprocessors:
    df = preprocessor.fit_transform(df)

# store the results
df.to_csv(args.output_file, index = False, quoting = csv.QUOTE_NONNUMERIC, line_terminator = "\n")

# create a pipeline if necessary and store it as pickle file
if args.export_file is not None:
    pipeline = make_pipeline(*preprocessors)
    with open(args.export_file, 'wb') as f_out:
        pickle.dump(pipeline, f_out)