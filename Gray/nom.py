from Gray import read_image

image,x,y=read_image('d.png')

pixels=[]
for i in range(x):
    for j in range(y):
        pixel=image.getpixel((i,j))
        pixels.append((pixel))
pixel_max=max(pixels)
pixel_min=min(pixels)

table=[]
for i in range(256):
    table.append(200*(i-pixel_min)/(pixel_max-pixel_min))
image=image.point(table,'L')
image.save('d_nom.png')