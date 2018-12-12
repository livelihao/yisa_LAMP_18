## YISA Final
文件说明

## 原始数据
### imges_orginal/image
训练数据的原始图像（10000）

### laebles.txt
训练数据的原始标签txt文件

### images/image
复赛试题图像

## py程序说明及中间处理文件
### retrain.py
重训练文件 使用retrain.sh来重新训练Inception V3网络

### model_dir/
Inception V3网络

### bottlenecks/image
Inception V3网络训练后的图像的特征（10000,2048）

### image_labels_dir/
Inception V3网络需要的特征文件夹，选取特征过程不需要，可以为空

### image_test/
测试文件顺序创建的文件夹

### log/
Inception V3网络训练过程log文件

### Model/
Inception V3网络模型

### bottlen_handle.py
将图像特征导入至bottlencks.csv文件中

### img_data.py
统计并查看image的信息

### img_handle.py
尺寸归一化image（可以不需要）（已经abandon）

### txt_handle.py
针对多标签神经网络的txt构建（已经abandon）

### check_order.py
检查文件的顺序是否和label.txt的顺序一致

### randomtree_**_smo.py
随机森林模型，使用SMOTE对数据进行平衡

### pro_**.csv
预测的概率文件，为最后的输出提供数据

### retrained_graph.pb
神经网络模型图

### str_out.txt
格式处理后并提交的文件

### target.csv
使用txt_handle.py 从train.txt中提出的标签文件，并且删除了image名字列

### tmp*.txt 
测试顺序的临时文件





