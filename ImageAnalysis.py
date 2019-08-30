
"""
Anne Marie Pruett
"""

import numpy as np
import matplotlib.pyplot as mplot
from PIL import Image #imports Python Image Library
import os

#create threshhold variable and set it equal to -1 so it fails while loop
threshhold=-1
#while loop to check if user input for threshhold is valid
while threshhold<0 or threshhold>255:
    string1=input("What is your threshhold variable?")
    threshhold=float(string1)#convert string input to float

imageList=[]#list to hold all of the images
#go through directory where images are and open,convert to numerical matrices
#and add to imageList
for file in os.listdir("/Users/amepruett/Documents/rebelmrkt"):
    if (file!=".DS_Store"):
        image=Image.open("/Users/amepruett/Documents/rebelmrkt/"+file)
        image=np.float32(image)
        imageList.append(image)

#create a variable for average image and set it equal to first image in imageList
ave_img=imageList[0]
#loop through every item in imageList and add to ave_img
for index in range(1,len(imageList)) :
    ave_img+=imageList[index]
#divide ave_image by the length of imageList
ave_img/=len(imageList)

#calculate the standartd deviation of the images
#loop through all of the items in imageList,subtract ave_img, and square the resulting #
std_dev=np.square(imageList[0]-ave_img)
for i in range(1,len(imageList)):
    std_dev+=np.square(imageList[i]-ave_img)
    
#divide std_dev by the number of items in the list 
std_dev/=(len(imageList))
#get the square root of std_dev
std_dev=np.sqrt(std_dev)


#loops over each row of the ave_img
for row in range(0, len(ave_img)):
 #loops over each column of the ave_img
     for col in range(0, len(ave_img[row])):
 #if the pixel at position [row][col] has any
 #color elements with a std_dev above threshhold
         if (std_dev[row][col] > [threshhold,threshhold , threshhold]).any():
 #if so, then we set that pixel's color to Cyan in the ave_img
             ave_img[row][col]=[255.0, 0.0, 0.0]

#clips all pixel values to be between 0 and 255 
ave_img=np.clip(ave_img, 0, 255)
#converts the image from a 32-bit float to an
#unsigned 8-bit integer
ave_img=np.uint8(ave_img)

#display the average image
mplot.imshow(ave_img)
mplot.show() 




     
