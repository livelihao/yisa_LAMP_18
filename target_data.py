# -*- coding:utf-8 -*-

import os
import json
from pandas.io.json import json_normalize
import pandas as pd
ImagePath = "./train/"

realpath = os.path.realpath
labelpath = "./train.txt"
ImagePathGray = "./train_out/"

txt = []
with open(labelpath, 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
            pass
        txt.append(line)

txt = txt[0]
labels =[]
for t in txt.replace('[','').replace('{"data":','').replace(']}',',').split('},'):
    if  t:
        t = t+'}'
        label = json.loads(t)
        labels.append(label)
labels.sort(key=lambda k:(k.get('image', 0)))
# print(labels)

for i in range(6):
    df = json_normalize(labels)
# print(df.apply(pd.value_counts))
# print(df.describe())
print(df['daibao'].value_counts())
print(df['kouzhao'].value_counts())
print(df['laxiang'].value_counts())
print(df['maozi'].value_counts())
print(df['yanjing'].value_counts())

# df['**'].value_counts()

# print(lb1)

# print(df[4000:].describe())
# bt=pd.read_csv('./bottlenecks.csv')
# print(bt.describe())
df[4000:].to_csv('./target_train.csv', index=0)
df[:4000].to_csv('./target_test.csv', index=0)