from Gray import read_image
import math
image,x,y=read_image('c.png')
table=[]
for i in range(256):
    table.append(40*math.log1p(i))

image=image.point(table,'L')
image.save('c_log.png')