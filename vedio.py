from random import randint
from PIL import Image
import numpy
import cv2
import os

x=input("enter path only(default=>'img.jpg')") or "img.jpg"
print("processing.......")
y=20
noofframe=50
image=Image.open(x)
image.thumbnail((1000, 700))
Image_data = numpy.asarray(image)
tel=Image.open("televizor.jpg")
vedio = cv2.VideoWriter("video.mp4",cv2.VideoWriter_fourcc(*'mp4v'),7,tel.size)
zero = [len(Image_data[0][0])*list([0])]*len(Image_data[0])
zero1 =  len(Image_data[0][0])*list([0])
for k in range(noofframe):
    frame = Image_data.copy()
    tel=Image.open("televizor.jpg")
    for i in range(len(Image_data)//y):
        for j in range(y//10):
            random=randint(0,y-1)
            frame[(y*i)+random] = zero
    for i in range(len(Image_data)):
        for j in range(len(Image_data[0])//4):
            random = randint(0,len(Image_data[0])-1)
            frame[i][random]=zero1
    tel.paste(Image.fromarray(frame),(340+(1000//2)-(image.size[0]//2),360))
    newImg = numpy.asarray(tel)
    newImg = cv2.cvtColor(newImg, cv2.COLOR_RGB2BGR)
    vedio.write(newImg)
    print(k+1,"/",noofframe)
vedio.release()
print("done!!!")