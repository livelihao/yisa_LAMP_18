#-*- coding:utf-8 -*-
import os
from PIL import Image

ImagePath = "./test/"
imagelist = os.listdir(ImagePath)
realpath = os.path.realpath

w_s = 128
h_s = 256

count=1

for image in imagelist:
    im = Image.open(ImagePath + '/' + image)
    out = im.resize((w_s, h_s), Image.ANTIALIAS)
    if count>4000:
        out.save("./images/image" + '/' + str(count) +'.jpg')
    else:
        out.save("./images_origin" + '/' + str(count) + '.jpg')

    count+=1

print(count)
