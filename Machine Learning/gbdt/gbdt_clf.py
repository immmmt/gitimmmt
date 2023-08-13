from sklearn.datasets import make_hastie_10_2
from sklearn.ensemble import GradientBoostingClassifier

X, y = make_hastie_10_2(random_state=0)
print(X.shape, y.shape)
X_train, X_test = X[:10000], X[10000:]
y_train, y_test = y[:10000], y[10000:]

clf = GradientBoostingClassifier(n_estimators=500, learning_rate=1.0, max_depth=2, random_state=0).fit(X_train, y_train)
print(clf.score(X_test, y_test))
