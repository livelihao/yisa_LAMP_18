import os
import time
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, f1_score, precision_score, recall_score
from sklearn.ensemble import RandomForestClassifier

bottlenecks = pd.read_csv('./bottlenecks.csv')
targets = pd.read_csv('./target.csv')
daibao = targets['daibao']
kouzhao = targets['kouzhao']
laxiang = targets['laxiang']
maozi = targets['maozi']
yanjing = targets['yanjing']

RANDOM_STATE = 500
X_train, X_test, y_db_train, y_db_test = train_test_split(bottlenecks, yanjing, test_size=0.15, random_state=RANDOM_STATE)
ss = StandardScaler()
X_train = ss.fit_transform(X_train)
X_test = ss.transform(X_test)

t1 = time.time()

clf = RandomForestClassifier(n_estimators=50, max_depth=3, random_state=RANDOM_STATE).fit(X_train, y_db_train)

predict = clf.predict(X_test)

print(clf.score(X_test, y_db_test))
print('****************metrics***************')
print(classification_report(y_db_test, predict))
print('-------precision_score:')
print(precision_score(y_db_test, predict, average='binary'))
print('-------recall_score:')
print(recall_score(y_db_test, predict, average='binary'))
print('-------F1_score:')
print(f1_score(y_db_test, predict))
print('-------time:')
t2 = time.time()
print(t2-t1)
