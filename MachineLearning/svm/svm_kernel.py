# -*- encoding:utf-8 -*-
from sklearn import svm
from sklearn import datasets
from sklearn.model_selection import train_test_split as ts

'''
‘linear’:线性核函数
‘poly’：多项式核函数
‘rbf’：径像核函数/高斯核
‘sigmod’:sigmod核函数
‘precomputed’:核矩阵
'''
# import our data
iris = datasets.load_iris()
X = iris.data
y = iris.target

# split the data to  7:3
X_train, X_test, y_train, y_test = ts(X, y, test_size=0.3)
print(y_test)
# select different type of kernel function and compare the score

# kernel = 'rbf'
clf_rbf = svm.SVC(kernel='rbf')
clf_rbf.fit(X_train, y_train)
score_rbf = clf_rbf.score(X_test, y_test)
print("The score of rbf is : %f" % score_rbf)

# kernel = 'linear'
clf_linear = svm.SVC(kernel='linear')
clf_linear.fit(X_train, y_train)
score_linear = clf_linear.score(X_test, y_test)
print("The score of linear is : %f" % score_linear)

# kernel = 'poly'
clf_poly = svm.SVC(kernel='poly')
clf_poly.fit(X_train, y_train)
score_poly = clf_poly.score(X_test, y_test)
print("The score of poly is : %f" % score_poly)

# kernel = 'sigmoid'
clf_sigmoid = svm.SVC(kernel='sigmoid')
clf_sigmoid.fit(X_train, y_train)
score_sigmoid = clf_sigmoid.score(X_test, y_test)
print("The score of sigmoid is : %f" % score_sigmoid)

# precomputed
clf_precomputed = svm.SVC(kernel='sigmoid')
clf_precomputed.fit(X_train, y_train)
score_precomputed = clf_precomputed.score(X_test, y_test)
print("The score of precomputed is : %f" % score_precomputed)