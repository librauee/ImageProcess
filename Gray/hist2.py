from Gray import read_image
import pandas as pd
import matplotlib.pyplot as plt


# 原图
image,x,y=read_image('g.png')
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

plt.subplot(221)
plt.hist(pixels,bins=256)

# 目标图片
image,x,y=read_image('g2.png')
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

table2=[]
for i in range(256):
    table2.append(hist_dict[i]*255)

# 直方图规定化
table=[round(x) for x in table]
table2=[round(x) for x in table2]
new_table=[]
for i in range(256):
    flag=True
    for j in range(256):
        if table[i]==table2[j]:
            new_table.append(j)
            flag=False
            break
    if flag:
        temp=255
        for j in range(256):
            if abs(table[i]-table2[j])<temp:
                temp=abs(table[i]-table2[j])
                min_j=j
        new_table.append(min_j)



plt.subplot(222)
plt.hist(pixels,bins=256)

image,x,y=read_image('g.png')
image=image.point(new_table,'L')
image.save('new_g.png')

image,x,y=read_image('new_g.png')
pixels=[]
for i in range(x):
    for j in range(y):
        pixel=image.getpixel((i,j))
        pixels.append((pixel))


plt.subplot(223)
plt.hist(pixels,bins=256)
plt.show()