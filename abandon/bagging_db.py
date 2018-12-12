import os
import time
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, f1_score, precision_score, recall_score

bottlenecks = pd.read_csv('./bottlenecks.csv')
targets = pd.read_csv('./target.csv')
daibao = targets['daibao']
kouzhao = targets['kouzhao']
laxiang = targets['laxiang']
maozi = targets['maozi']
yanjing = targets['yanjing']

RANDOM_STATE = 500
X_train, X_test, y_db_train, y_db_test = train_test_split(bottlenecks, daibao, test_size=0.15, random_state=RANDOM_STATE)
ss = StandardScaler()
X_train = ss.fit_transform(X_train)
X_test = ss.transform(X_test)

t1 = time.time()
# clf = DecisionTreeClassifier().fit(X_train, y_db_train)
clf_db = BaggingClassifier(base_estimator= DecisionTreeClassifier(), max_samples=0.5, max_features=0.5).fit(X_train, y_db_train)

# predict = clf.predict(X_test)
predict = clf_db.predict(X_test)

# print(clf.score(X_test, y_db_test))
print('****************metrics***************')
print(classification_report(y_db_test, predict))
print('-------precision_score:')
print(precision_score(y_db_test, predict))
print('-------recall_score:')
print(recall_score(y_db_test, predict))
print('-------F1_score:')
print(f1_score(y_db_test, predict))
print('------------time:')
print(time.time()-t1)
