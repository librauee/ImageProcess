from PIL import Image
import math

def read_image(img_path):
    image=Image.open(img_path)
    image=image.convert('L')
    x=image.size[0]
    y=image.size[1]
    return image,x,y


table = []
# for i in range(256):
#     #table.append(255-i)
#     if i < 50:
#         table.append(0)
#     elif i>200:
#         table.append(255)
#     else:
#         table.append(i)
# for i in range(256):
#     table.append(40*math.log1p(i))



#
# import pandas as pd
#
# pixels= pd.Series(pixels)
#
# countDict = dict(pixels.value_counts())
# proportitionDict = dict(pixels.value_counts(normalize=True))
#
# print(countDict)
# print(proportitionDict)
# hist_dict={}
# add=0
# for i in range(256):
#     if i in proportitionDict.keys():
#         add+=proportitionDict[i]
#     hist_dict[i]=add
#
# print(hist_dict)
#
# for i in range(256):
#     table.append(hist_dict[i]*255)
# print(table)
# image = image.point(table,'L')
# image.show()
# import random
# for i in range(x):
#     for j in range(y):
#         pixel=image.getpixel((i,j))
#         if random.random()>0.98:
#             image.putpixel((i,j),255 if random.random()>0.5 else 0)
#         else:
#             image.putpixel((i, j),pixel)
# image.show()