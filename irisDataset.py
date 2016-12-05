#import a dataset
from sklearn.datasets import load_iris
iris = load_iris()pana

from sklearn.model_selection import train_test_split
#from sklearn.metrics import accuracy
from sklearn import tree

X = iris.data
y = iris.target


X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.5)
clf = tree.DecisionTreeClassifier().fit(X_train, y_train)


#print iris.data
print iris.feature_names
print iris.target_names
print clf.predict([[5.2, 3.1, 1.9, 0.6]])
