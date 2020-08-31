from sklearn import tree
import numpy as np

labels = np.array([0, 1, 0,])
data = np.array([
                 [1160.1425737,-293.91754364,48.57839763,-8.71197531],
                 [1269.12244319,15.63018184,-35.39453423,17.86128323],
                 [995.79388896,39.15674324,-1.70975298,4.1993401]
                 ])

clf_tree1 = tree.DecisionTreeClassifier()
reg_tree1 = tree.DecisionTreeRegressor()
clf_tree2 = tree.DecisionTreeClassifier(
  max_depth=8)  # max depth of 8
reg_tree2 = tree.DecisionTreeRegressor(
  max_depth=5)  # max depth of 5

clf_tree1.fit(data, labels)