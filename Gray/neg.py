from Gray import read_image

image,x,y=read_image('a.png')
for i in range(x):
    for j in range(y):
        pixel=image.getpixel((i,j))
        image.putpixel((i,j),255-pixel)
image.save('a_neg.png')