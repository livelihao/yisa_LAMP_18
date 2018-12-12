from __future__ import division

def text_create(name, msg):
    desktop_path = './test/'
    full_path = desktop_path + name + '.txt'
    file = open(full_path, 'w')
    for i in range(len(msg)):
        label = msg[i]
        file.write(label + '\n')
    file.close()
    print('Done')

count=0
f = open("target.csv", 'r')
# f = open("labels.txt", 'r')

while 1:
    lines = f.readlines()  # 逐行读取整个文件
    n = 1  # n表示读入的第几行
    for line in lines:
        if line:
            # 字符字典，数字表示负号前面有多少个1，例如0就对应没有1即字符desert
            total_labels = {0: "daibao", 2: "kouzhao", 3: "laxiang", 4: "maozi", 5: "yanjing"}
            output_labels = []  # 最终输出的列表
            line = line.split(',')  # 将每行按照1进行分开
            label_count = []  # 每个负号前面有多少个1的列表
            for i in range(len(line)):
                if line[i] == "1":
                    label_count.append(i)
            for i in range(0, 5):
                if i in label_count:  # 如果输出的列表中存在字典里的数字，那么就代表存在某个字符
                    output_labels.append(total_labels[i])
            print(line[1], output_labels)
            text_create(str(line[1]), output_labels)
            n = n + 1
    else:
        break
f.close()