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
* precicion-recall (PR) area under the curve - useful for imbalanced classification problems, plots precision against recall and in order to obtain one value for comparison, we calculate the AUC (this is similar to well-known ROC but PR is argued to be more robust on imbalanced date hence we opt for PR instead of ROC)
  * less than 0.5 considered to belong to a bad classifier
  * around 0.5 random guessing classifier
  * close to 1 good classifier 
  (might want to double-check interpretation of metrics again) 
* matthews correlation coefficient (MCC) - similarily to f1 and f2 scores and precicion-recall curves the MCC also uses values of the confusion matrix, however, it uses all four values for its evaluation making it especially robust for imbalanced class distribution, the metric works after the principle the higher the correlation between prediction and actual label, the better the prediction
  * 1 is perfect correlation - the classifier always predicts correctly
  * 0 is random guessing
  * -1 is perfect negative correlation - the classifier always missclassifes 
  

### Schema

Given from point of departure: 
* split data into train, test and validation set

Maybe add for further analysis (not done yet):
* cross validation - more computationally expensive

### Baseline

Given from point of departure:
* majority class classifier
* label frequency classifier 
