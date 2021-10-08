# Documentation of Data Science Tweets Classification for MLinpractice

October 06 2021 

## Evaluation 

### Metrics 

Given from point of departure:
* accuracy - kept for completeness but not suitable for imbalanced data
* cohen's kappa - degree of agreement between two raters (true labels vs predicted labels ?) for rating the same content, taking into account how often these raters may agree by chance
  * below zero - less agreement than random chance
  * zero - random agreement
  * one - perfect agreement 

Added for further analysis:
* balanced accuracy - takes precision and recall into account, good for imbalanced data
* f1- score and f2-score - measure of precision and recall, f2 might be useful since it takes false-negatives more into account (here we want to avoid missing out on tweets that would go viral)
* precicion-recall area under the curve - useful for imbalanced classification problems, plots precision against recall and in order to obtain one value for comparison, we calculate the AUC 
  * less than 0.5 considered to belong to a bad classifier
  * around 0.5 random guessing classifier
  * close to 1 good classifier 
  (might want to double-check interpretation of metrics again) 
  

### Schema

Given from point of departure: 
* split data into train, test and validation set

Maybe add for further analysis (not done yet):
* cross validation - more computationally expensive

### Baseline

Given from point of departure:
* majority class classifier
* label frequency classifier 
