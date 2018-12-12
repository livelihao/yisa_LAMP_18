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
from collections import Counter
from imblearn.ensemble import EasyEnsemble
from imblearn.over_sampling import SMOTE

RANDOM_STATE = 500
bottlenecks = pd.read_csv('./bottlenecks_train.csv')
targets = pd.read_csv('./target_train.csv')
daibao = targets['daibao']
kouzhao = targets['kouzhao']
laxiang = targets['laxiang']
maozi = targets['maozi']
yanjing = targets['yanjing']
bn_test = pd.read_csv('./bottlenecks.csv')
targets_test = pd.read_csv('./target_test.csv')
db_test = targets_test['daibao']

print(targets_test.describe())
smo = SMOTE(random_state=RANDOM_STATE)
bottlenecks, daibao = smo.fit_sample(bottlenecks, daibao)

X_train, X_test, y_db_train, y_db_test = train_test_split(bottlenecks, daibao, test_size=0.15, random_state=RANDOM_STATE)

print(db_test.shape)
print(bn_test.shape)
ss = StandardScaler()
X_train = ss.fit_transform(X_train)
X_test = ss.transform(X_test)
bn_test = ss.transform(bn_test)
print(X_train.shape)

t1 = time.time()

clf = RandomForestClassifier(n_estimators=50, max_depth=20, random_state=RANDOM_STATE).fit(X_train, y_db_train)

predict = clf.predict(X_test)
pre = clf.predict(bn_test)

print(pre)
print(clf.score(bn_test, db_test))
print('###################')
print(classification_report(db_test, pre))


print(clf.score(X_test, y_db_test))
print('****************metrics***************')
print(classification_report(y_db_test, predict))
print('-------precision_score:')
print(precision_score(y_db_test, predict))
print('-------recall_score:')
print(recall_score(y_db_test, predict))
print('-------F1_score:')
print(f1_score(y_db_test, predict))
print('-------time:')
t2 = time.time()



print(t2-t1)

# pro = clf.predict_proba(X_test)
# pd.DataFrame(pro).to_csv('./pro_kz.csv', index=0)