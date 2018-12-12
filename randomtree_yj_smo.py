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
targets = pd.read_csv('./target.csv')
daibao = targets['daibao']
kouzhao = targets['kouzhao']
laxiang = targets['laxiang']
maozi = targets['maozi']
yanjing = targets['yanjing']
X_test = pd.read_csv('./bottlenecks.csv')

smo = SMOTE(random_state=RANDOM_STATE)
X_train, y_db_train = smo.fit_sample(bottlenecks, yanjing)

ss = StandardScaler()
X_train = ss.fit_transform(X_train)
X_test = ss.transform(X_test)

# print(X_train.shape)

t1 = time.time()

clf = RandomForestClassifier(n_estimators=50, max_depth=20, random_state=RANDOM_STATE).fit(X_train, y_db_train)
pro = clf.predict_proba(X_test)
pd.DataFrame(pro).to_csv('./pro_yj.csv', index=0)

print('-------time:')
t2 = time.time()
print(t2-t1)
