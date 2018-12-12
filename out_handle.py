import os
import pandas as pd
import numpy as np

imagelist = os.listdir('./images/image/')

pro_db = pd.read_csv('./pro_db.csv').values
pro_kz = pd.read_csv('./pro_kz.csv').values
pro_lx = pd.read_csv('./pro_lx.csv').values
pro_mz = pd.read_csv('./pro_mz.csv').values
pro_yj = pd.read_csv('./pro_yj.csv').values
print('read done!')

pre_db = [i for i in np.argmax(pro_db, axis=1)]
pre_kz = [i for i in np.argmax(pro_kz, axis=1)]
pre_lx = [i for i in np.argmax(pro_lx, axis=1)]
pre_mz = [i for i in np.argmax(pro_mz, axis=1)]
pre_yj = [i for i in np.argmax(pro_yj, axis=1)]

mx_db = pro_db.max(axis=1)
mx_kz = pro_kz.max(axis=1)
mx_lx = pro_lx.max(axis=1)
mx_mz = pro_mz.max(axis=1)
mx_yj = pro_yj.max(axis=1)

with open('str_out.txt', 'w') as f:
    f.write('{"data":[')
    for i in range(len(imagelist)):
    # for i in range(200):
        """
        {"image": "e515b069e9be930db6499c6af3d14d697bf6ae11.jpg
        ", "maozi": "1", "maozi_prob": 0.94291
        , "kouzhao": "0", "kouzhao_prob": 0.891221
        , "yanjing": "1", "yanjing_prob": 0.91442
        , "daibao": "0", "daibao_prob": 0.9133,
         "laxiang": "0", "laxiang_prob": 0.9931}
        """
        # if i == 199:
        if i+1 == len(imagelist):

            str_json = '{"image": "' + str(imagelist[i]) \
                       + '", "maozi": "' + str(pre_mz[i]) + '", "maozi_prob": ' + str(mx_mz[i]) \
                       + ', "kouzhao": "' + str(pre_kz[i]) + '", "kouzhao_prob": ' + str(mx_kz[i]) \
                       + ', "yanjing": "' + str(pre_yj[i]) + '", "yanjing_prob": ' + str(mx_yj[i]) \
                       + ', "daibao": "' + str(pre_db[i]) + '", "daibao_prob": ' + str(mx_db[i]) \
                       + ', "laxiang": "' + str(pre_lx[i]) + '", "laxiang_prob": ' + str(mx_lx[i]) \
                       + '}'
        else:
            str_json = '{"image": "' + str(imagelist[i]) \
                       + '", "maozi": "' + str(pre_mz[i]) + '", "maozi_prob": ' + str(mx_mz[i]) \
                       + ', "kouzhao": "' + str(pre_kz[i]) + '", "kouzhao_prob": ' + str(mx_kz[i]) \
                       + ', "yanjing": "' + str(pre_yj[i]) + '", "yanjing_prob": ' + str(mx_yj[i]) \
                       + ', "daibao": "' + str(pre_db[i]) + '", "daibao_prob": ' + str(mx_db[i]) \
                       + ', "laxiang": "' + str(pre_lx[i]) + '", "laxiang_prob": ' + str(mx_lx[i]) \
                       + '},'

        f.write(str_json)

    f.write(']}')



