from Gray import read_image

image,x,y=read_image('b.png')
table=[]
for i in range(256):
    table.append(i**0.5)

image=image.point(table,'L')
image.save('b_pow.png')

