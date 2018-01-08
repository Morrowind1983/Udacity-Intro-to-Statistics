#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn import tree
from sklearn.metrics import accuracy_score

print "features:", len(features_train[0])

clf = tree.DecisionTreeClassifier(criterion='entropy', min_samples_split=40)

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t1 = time()
pred = clf.predict(features_test)
print "predict time:", round(time()-t1, 3), "s"

score = accuracy_score(labels_test, pred)
print "accuracy score:", score

#########################################################

# no. of Chris training emails: 7936
# no. of Sara training emails: 7884
# features: 3785
# training time: 21.138 s
# predict time: 0.031 s
# accuracy score: 0.973833902162
