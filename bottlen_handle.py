import os
import pandas as pd

bottlenecks_path = './bottlenecks/image/'
bottlenecks_list = os.listdir(bottlenecks_path)

bottlenecks_df = pd.DataFrame()
txts = []
for bottle in bottlenecks_list:
    with open(bottlenecks_path+bottle, 'r') as f:
        txt = []
        while 1:
            line = f.readline()
            if not line:
                break
                pass
            txt.append(line)
        txt = txt[0].split(',')
        txts.append(txt)
    print(bottle)

print(len(txts))
bottlenecks_df = pd.DataFrame(txts)
print(bottlenecks_df)
bottlenecks_df.to_csv('./bottlenecks.csv', index=0)
