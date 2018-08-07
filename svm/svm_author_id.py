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




#########################################################
### your code goes here ###

from sklearn import svm
clf = svm.SVC(C=10000.0, kernel = 'rbf')

## features_train = features_train[:len(features_train)/100]
## labels_train = labels_train[:len(labels_train)/100]

print("Training ...")
t0 = time()
clf.fit(features_train,labels_train)
print "training time:", round(time()-t0, 3), "s"
print("Finished training ...")

t1 = time()
pred = clf.predict(features_test)
print "prediction time:", round(time()-t1, 3), "s"

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(pred, labels_test)
print "Accuracy: ", accuracy

print "Prediction 10: ", pred[10]
print "Prediction 26: ", pred[26]
print "Prediction 50: ", pred[50]

#########################################################


## training time: 292.522 s
## prediction time: 31.623 s
## Accuracy: 0.9840728100113766

## With 1% of the training set:
## training time: 1.371 s
## prediction time: 2.542 s
## Accuracy:  0.8845278725824801

## With 1% of the training set and rbf:
## training time: 0.232 s
## prediction time: 2.428 s
## Accuracy:  0.6160409556313993

## With C = 10.0
## training time: 0.288 s
## prediction time: 2.56 s
## Accuracy:  0.6160409556313993

## With C = 100.0
## training time: 0.229 s
## prediction time: 2.103 s
## Accuracy:  0.6160409556313993

## With C = 1000.0
## training time: 0.341 s
## prediction time: 2.054 s
## Accuracy:  0.8213879408418657

## With C = 10000.0
## training time: 0.23 s
## prediction time: 1.708 s
## Accuracy:  0.8924914675767918


## With C = 10000.0 and full training set
## training time: 194.512 s
## prediction time: 19.758 s
## Accuracy:  0.9908987485779295

## Prediction 10:  1
## Prediction 26:  0
## Prediction 50:  1

## sum(pred)
## 877
