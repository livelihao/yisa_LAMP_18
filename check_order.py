import os
import pandas as pd
import numpy as np
import json
from pandas.io.json import json_normalize

imagelist = os.listdir('./images/image/')

# str_imge = []
# for image in imagelist:
#     str_imge.append(image)
#
# print(str_imge)
# with open('tmp.txt', 'w') as f:
#     f.write(str(str_imge))

labelpath = "./train.txt"

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
print(labels)
for i in range(6):
    df = json_normalize(labels)

image_df = df['image']
with open('tmp2.txt', 'w') as f:
    for i in range(100):
        f.write("'"+str(image_df[i])+"', ")