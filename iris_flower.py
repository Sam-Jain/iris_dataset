from sklearn import datasets
import sklearn as sk
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

iris = datasets.load_iris()
X_iris, Y_iris = iris.data, iris.target

print X_iris.shape, Y_iris.shape
print X_iris[0], Y_iris[0]

