#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
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

features_train = features_train[:len(features_train)/100]
labels_train = labels_train[:len(labels_train)/100]


#########################################################
### your code goes here ###
from sklearn import svm
from sklearn.metrics import accuracy_score

clf = svm.SVC(C=10.0, kernel='rbf')

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
# training time: 0.15 s
# predict time: 1.708 s
# accuracy score: 0.616040955631
