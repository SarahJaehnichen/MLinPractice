#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reads in the original csv files and creates labels for the data points.
Stores the result as a single pandas DataFrame in a pickle file.

Created on Tue Sep 28 15:55:44 2021

@author: ml
"""

import os, argparse
import pandas as pd

# setting up CLI
parser = argparse.ArgumentParser(description = "Creation of Labels")
parser.add_argument("data_directory", help = "directory where the original csv files reside")
parser.add_argument("output_file", help = "path to the output csv file")
parser.add_argument("-l", '--likes_weight', help = "weight of likes", default = 1)
parser.add_argument("-r", '--retweet_weight', help = "weight of retweets", default = 1)
parser.add_argument("-t", '--threshold', help = "threshold to surpass for positive class", default = 50)
args = parser.parse_args()

# constants for relevant column names
COLUMN_LIKES = "likes_count"
COLUMN_RETWEETS = "retweets_count"
COLUMN_LABEL = "label"

# get all csv files in data_directory
file_paths = [args.data_directory + f for f in os.listdir(args.data_directory) if f.endswith(".csv")]

# load all csv files
dfs = []
for file_path in file_paths:
    dfs.append(pd.read_csv(file_path))

# join all data into a single DataFrame
df = pd.concat(dfs)

# compute new column "label" based on likes and retweets
df[COLUMN_LABEL] = (args.likes_weight * df[COLUMN_LIKES] + args.retweet_weight * df[COLUMN_RETWEETS]) > args.threshold

# store the DataFrame into a pickle file
df.to_csv(args.output_file)