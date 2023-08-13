from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split

wine = load_wine()
X = wine.data
Y = wine.target

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=2023)

model = RandomForestClassifier(n_estimators=100)
model_tree = DecisionTreeClassifier()
model.fit(X_train, y_train)
model_tree.fit(X_train, y_train)
score = model.score(X_test, y_test)
score_tree = model_tree.score(X_test, y_test)
print('随机森林：', score)
print('决策树：', score_tree)
print()