__author__ = 'jack'

import TestTrees as trees
import TestTreePlotter as plotter

#myTree = plotter.retrieveTree(0)
#myTree['no surfacing'][3] = 'maybe'
#plotter.createPlot(myTree)
#print myTree
#print plotter.getNumLeafs(myTree)
#print plotter.getTreeDepth(myTree)
#import trees

myDat, labels = trees.createDataSet()
myTree = plotter.retrieveTree(0)

trees.storeTree(myTree, './classify.txt')
print(trees.grabTree('./classify.txt'))
#print myTree

#print trees.classify(myTree, labels, [1, 1])

#print(myDat)
#print(labels)

#myTree = trees.createTree(myDat, labels)
#print(myTree)