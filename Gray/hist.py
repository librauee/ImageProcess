from Gray import read_image
import pandas as pd
import matplotlib.pyplot as plt

image,x,y=read_image('e.png')
pixels=[]
for i in range(x):
    for j in range(y):
        pixel=image.getpixel((i,j))
        pixels.append((pixel))

pixels=pd.Series(pixels)
proportitionDict=dict(pixels.value_counts(normalize=True))

hist_dict={}
add=0
for i in range(256):
    if i in proportitionDict.keys():
        add+=proportitionDict[i]
    hist_dict[i]=add

table=[]
for i in range(256):
    table.append(hist_dict[i]*255)
print(table)
image = image.point(table,'L')
image.show()
image.save('e_hist.png')
