#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Train or evaluate a single classifier with its given set of hyperparameters.

Created on Wed Sep 29 14:23:48 2021

@author: lbechberger
"""

import argparse, pickle
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score, cohen_kappa_score, balanced_accuracy_score, f1_score, fbeta_score, precision_recall_curve, auc, matthews_corrcoef

# setting up CLI
parser = argparse.ArgumentParser(description = "Classifier")
parser.add_argument("input_file", help = "path to the input pickle file")
parser.add_argument("-s", '--seed', type = int, help = "seed for the random number generator", default = None)
parser.add_argument("-e", "--export_file", help = "export the trained classifier to the given location", default = None)
parser.add_argument("-i", "--import_file", help = "import a trained classifier from the given location", default = None)
parser.add_argument("-m", "--majority", action = "store_true", help = "majority class classifier")
parser.add_argument("-f", "--frequency", action = "store_true", help = "label frequency classifier")
parser.add_argument("-a", "--accuracy", action = "store_true", help = "evaluate using accuracy")
parser.add_argument("-k", "--kappa", action = "store_true", help = "evaluate using Cohen's kappa") 
parser.add_argument("-b", "--balanced_accuracy", action = "store_true", help = "evaluate using balanced accuracy") 
parser.add_argument("-f_1", "--f_1", action = "store_true", help = "evaluate using f1-score") 
parser.add_argument("-f_2", "--f_2", action = "store_true", help = "evaluate using f2-score") 
parser.add_argument("-mcc", "--matthews_corrcoef", action = "store_true", help = "evaluate using matthews correlation coefficient")
parser.add_argument("-pr", "--prec_recall_auc", action = "store_true", help = "evaluate using precision-recall area under the curve")
args = parser.parse_args()

# load data
with open(args.input_file, 'rb') as f_in:
    data = pickle.load(f_in)

if args.import_file is not None:
    # import a pre-trained classifier
    with open(args.import_file, 'rb') as f_in:
        classifier = pickle.load(f_in)

else:   # manually set up a classifier
    
    if args.majority:
        # majority vote classifier
        print("    majority vote classifier")
        classifier = DummyClassifier(strategy = "most_frequent", random_state = args.seed)
        classifier.fit(data["features"], data["labels"])
    elif args.frequency:
        # label frequency classifier
        print("    label frequency classifier")
        classifier = DummyClassifier(strategy = "stratified", random_state = args.seed)
        classifier.fit(data["features"], data["labels"])

# now classify the given data
prediction = classifier.predict(data["features"])

# collect all evaluation metrics
evaluation_metrics = []
# standard accuracy
if args.accuracy:
    evaluation_metrics.append(("accuracy", accuracy_score(data["labels"], prediction)))
# cohen's kappa 
if args.kappa:
    evaluation_metrics.append(("Cohen's kappa", cohen_kappa_score(data["labels"], prediction)))
# balanced accuracy
if args.balanced_accuracy:
    evaluation_metrics.append(("balanced accuracy", balanced_accuracy_score(data["labels"], prediction)))
# f1-score
if args.f_1:
    evaluation_metrics.append(("f1 score", f1_score(data["labels"], prediction)))
# f2-score, other variants possible by changing beta 
if args.f_2:
    evaluation_metrics.append(("f2 score", fbeta_score(data["labels"], prediction, beta=2)))
# matthews correlation coefficient
if args.matthews_corrcoef:
    evaluation_metrics.append(("matthews corr-coefficient", matthews_corrcoef(data["labels"], prediction)))
# precision-recall area under the curve 
if args.prec_recall_auc:
    # first calculation of prec-recall-curve, thresholds unimportant for further calculations
    x_prec, y_rec, thresholds = precision_recall_curve(data["labels"], prediction)
    # calculation of AUC 
    evaluation_metrics.append(("precision recall AUC", auc(x_prec, y_rec)))

# compute and print them
for metric_name, metric_score in evaluation_metrics:
    print("    {0}: {1}".format(metric_name, metric_score))
    
# export the trained classifier if the user wants us to do so
if args.export_file is not None:
    with open(args.export_file, 'wb') as f_out:
        pickle.dump(classifier, f_out)