#-*- coding:utf-8 -*-
import os
from PIL import Image
ImagePath = "./train/"
imagelist = os.listdir(ImagePath)
realpath = os.path.realpath

t_w = 0;t_h = 0
avg_w = 0;avg_h = 0
count = 0
min_w = 10000; min_h = 10000
max_w = 0; max_h = 0
min_product = 111110; min_product_w = 0; min_product_h = 0
w_s = 100
h_s = 200

for image in imagelist:
    im = Image.open(ImagePath + '/' + image)
    t_w += im.size[0]
    t_h += im.size[1]
    if min_w > im.size[0]:
        min_w = im.size[0]
    if min_h > im.size[1]:
        min_h = im.size[1]
    if max_w < im.size[0]:
        max_w = im.size[0]
    if max_h < im.size[1]:
        max_h = im.size[1]
    if min_product > im.size[0] * im.size[1]:
        min_product = im.size[0] * im.size[1]
        min_product_w = im.size[0]
        min_product_h = im.size[1]
    count += 1

    # im = Image.open(ImagePath + '/' + image)
    # out = im.resize((w_s, h_s), Image.ANTIALIAS)
    # out.save("./train_out" + '/' + image)

avg_w = t_w / count
avg_h = t_h / count
print(avg_w)
print(avg_h)

print("avg_w={}\navg_h={}\nThe total number of image is {}".format(avg_w, avg_h, count))
print("The min width is {}\nThe max width is {}".format(min_w, max_w))
print("The min height is {}\nThe max height is {}".format(min_h, max_h))
print("The min image size is {}*{}".format(min_product_w, min_product_h))