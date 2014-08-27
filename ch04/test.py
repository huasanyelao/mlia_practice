from numpy import *

__author__ = 'jack'

import bayes

listOPosts,listClasses = bayes.loadDataSet()

myVocabList = bayes.createVocabList(listOPosts)

print myVocabList

#print bayes.setOfWords2Vec(myVocabList, listOPosts[0])

trainMat = []
for post in listOPosts:
    trainMat.append(bayes.setOfWords2Vec(myVocabList, post))

p0V, p1V, pAb = bayes.trainNB0(array(trainMat), array(listClasses))

print pAb
print p0V
print p1V

testEntry = ['love', 'my', 'dalmation']
thisDoc = array(bayes.setOfWords2Vec(myVocabList, testEntry))
print thisDoc
print testEntry, 'classsified as: ', bayes.classifyNB(thisDoc, p0V, p1V, pAb)

testEntry = ['stupid', 'garbage']
thisDoc = array(bayes.setOfWords2Vec(myVocabList, testEntry))
print thisDoc
print testEntry, 'classsified as: ', bayes.classifyNB(thisDoc, p0V, p1V, pAb)