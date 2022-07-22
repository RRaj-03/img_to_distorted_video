from random import randint
from PIL import Image
import numpy
import cv2

x=input("enter path only(default=>'img.jpg')") or "img.jpg"
print("processing.......")
image=Image.open(x)
image.thumbnail((1000, 700))
Image_data = numpy.asarray(image)
tel=Image.open("televizor.jpg")
vedio = cv2.VideoWriter("video.avi",cv2.VideoWriter_fourcc(*'DIVX'),7,tel.size)
zero = [len(Image_data[0][0])*list([0])]*len(Image_data[0])
# for k in range(90):
#     frame = Image_data.copy()
#     frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
#     for i in range(len(Image_data)//10):
#         for j in range(randint(0,10)):
#             frame[(10*i)+j] = zero
#     vedio.write(frame)
# vedio.release()
       
for k in range(90):
    frame = Image_data.copy()
    tel=Image.open("televizor.jpg")
    for i in range(len(Image_data)//10):
        for j in range(randint(0,10)):
            frame[(10*i)+j] = zero
    tel.paste(Image.fromarray(frame),(340+(1000//2)-(image.size[0]//2),360))
    newImg = numpy.asarray(tel)
    newImg = cv2.cvtColor(newImg, cv2.COLOR_RGB2BGR)
    vedio.write(newImg)
vedio.release()
print("done!!!")