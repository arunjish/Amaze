"""
===========================

"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

import matplotlib
import numpy
from PIL import Image
import matplotlib.pyplot as plt
import skimage.io as io

"load image data"

from skimage import color
RGBImage = io.imread('poops.jpg')
ImgGrey = color.rgb2gray(RGBImage)     # Gray image

def neighbours(x,y,image):
    "Return 8-neighbours of image point P1(x,y), in a clockwise order"
    img = image
    x_1, y_1, x1, y1 = x-1, y-1, x+1, y+1
    return [ img[x_1][y], img[x_1][y1], img[x][y1], img[x1][y1],     # P2,P3,P4,P5
                img[x1][y], img[x1][y_1], img[x][y_1], img[x_1][y_1] ]    # P6,P7,P8,P9

def transitions(neighbours):
    "No. of 0,1 patterns (transitions from 0 to 1) in the ordered sequence"
    n = neighbours + neighbours[0:1]      # P2, P3, ... , P8, P9, P2
    return sum( (n1, n2) == (0, 1) for n1, n2 in zip(n, n[1:]) )  # (P2,P3), (P3,P4), ... , (P8,P9), (P9,P2)

def zhangSuen(image):
    "the Zhang-Suen Thinning Algorithm"
    Image_Thinned = image.copy()  # deepcopy to protect the original image
    changing1 = changing2 = 1        #  the points to be removed (set as 0)
    while changing1 or changing2:   #  iterates until no further changes occur in the image
        # Step 1
        changing1 = []
        rows, columns = Image_Thinned.shape               # x for rows, y for columns
        for x in range(1, rows - 1):                     # No. of  rows
            for y in range(1, columns - 1):            # No. of columns
                P2,P3,P4,P5,P6,P7,P8,P9 = n = neighbours(x, y, Image_Thinned)
                if (Image_Thinned[x][y] == 1     and    # Condition 0: Point P1 in the object regions 
                    2 <= sum(n) <= 6   and    # Condition 1: 2<= N(P1) <= 6
                    transitions(n) == 1 and    # Condition 2: S(P1)=1  
                    P2 * P4 * P6 == 0  and    # Condition 3   
                    P4 * P6 * P8 == 0):         # Condition 4
                    changing1.append((x,y))
        for x, y in changing1: 
            Image_Thinned[x][y] = 0
        # Step 2
        changing2 = []
        for x in range(1, rows - 1):
            for y in range(1, columns - 1):
                P2,P3,P4,P5,P6,P7,P8,P9 = n = neighbours(x, y, Image_Thinned)
                if (Image_Thinned[x][y] == 1   and        # Condition 0
                    2 <= sum(n) <= 6  and       # Condition 1
                    transitions(n) == 1 and      # Condition 2
                    P2 * P4 * P8 == 0 and       # Condition 3
                    P2 * P6 * P8 == 0):            # Condition 4
                    changing2.append((x,y))    
        for x, y in changing2: 
            Image_Thinned[x][y] = 0
    return Image_Thinned



def getStopCordinates(RGBimage):
	im=numpy.asarray(RGBimage)

	shape= im.shape
	rows= shape[0]
	cols=shape[1]
	redCordinates=[]

	for i in range(rows-1,0,-1): 
		for j in range(cols-1,0,-1):
			if im[i][j][0]in range(200,256) and im[i][j][1] in range(0,50) and im[i][j][2] in range(0,50)  : 
				sys.stdout.write("red : "+ str(im[i][j]) +"("+str(i)+","+str(j)+")" + "\n ")
				redCordinates.append((i,j))
				if len(redCordinates) >15:
					return redCordinates
	return redCordinates

def getStartCordinates(RGBimage):
	im=numpy.asarray(RGBimage)

	shape= im.shape
	rows= shape[0]
	cols=shape[1]
	
	greenCordinates=[]

	for i in range(rows-1,0,-1): 
		for j in range(cols-1,0,-1):
			if im[i][j][0]in range(0,50) and im[i][j][1] in range(200,256) and im[i][j][2] in range(0,50)  : 
				sys.stdout.write("green : "+ str(im[i][j]) +"("+str(i)+","+str(j)+")" + "\n ")
				greenCordinates.append((i,j))
				if len(greenCordinates) >15:
					return greenCordinates
	return greenCordinates


def averageOfListOfCordinates(listOfCordinates):
	row=int(sum([item[0] for item in listOfCordinates]) / float(len(listOfCordinates)))
	col=int(sum([item[1] for item in listOfCordinates]) / float(len(listOfCordinates)))
	return (row,col)

def embbedStartAndEndToIntegerMatrix(image): # input ndarray of image or image itself -- output ndarray with start,end
	im=numpy.asarray(image)
	print im.shape
	print len(im)
	print len(im[0])
	imMatrix=[[0 for x in range(len(im[0])+10)] for y in range(len(im)+10)] 
	
	
	"get stop cordinates"

	stopCordinatesList= getStopCordinates(RGBImage) # return approximate stop cordinate list
	stopCordinate=averageOfListOfCordinates(stopCordinatesList) #return tuple of cordinate

	"get start cordinates"

	startCordinatesList= getStartCordinates(RGBImage) # return approximate stop cordinate list
	startCordinate=averageOfListOfCordinates(startCordinatesList) #return tuple of cordinate

	for x in range(0,len(im)):
		for y in range(0,len(im[0])):
			adress=(x,y)
			if adress == startCordinate :
				imMatrix[x][y]=3
				print adress 
				print imMatrix[x][y]
			elif adress == stopCordinate :
				imMatrix[x][y]=9
				print adress 
				print imMatrix[x][y]
			else:			
				if(im[x][y]==1):
					imMatrix[x][y]=1
				else:
					imMatrix[x][y]=0

			
					
	return imMatrix

def printImageUsingSymbols(image):
	#print array as . and #
	im=numpy.asarray(image)
	
	for x in range(0,len(im)):
		for y in range(0,len(im[0])):
			
			if im[x][y] == 3 :
				sys.stdout.write('<')
			elif im[x][y] == 9:
				sys.stdout.write('>')
			else:			
				if(im[x][y]==1):
					sys.stdout.write('#')
				else:
					sys.stdout.write('.')
			
				
		print('\n')
 
def printImageUsingZeorsAndOnes(image):
	im=numpy.asarray(image)
	for x in range(0,len(im)):
		for y in range(0,len(im[0])):
			if(im[x][y]==1):
				sys.stdout.write('1')
			else:
				sys.stdout.write('0')
		print('\n')



"Convert gray images to binary images using Otsu's method"
from skimage.filters import threshold_otsu
Otsu_Threshold = threshold_otsu(ImgGrey)   
BW_Original = ImgGrey < Otsu_Threshold    # must set object region as 1, background region as 0 !


"Apply the algorithm on images"
BW_Skeleton = zhangSuen(BW_Original)

im=numpy.asarray(BW_Skeleton)


startEndEmbbedMatrix = embbedStartAndEndToIntegerMatrix(BW_Skeleton)



"printing array"


printImageUsingSymbols(startEndEmbbedMatrix)

" print image-ndarray as zeros and ones "

#printImageUsingZeorsAndOnes(im)









"""
"Display the results"
fig, ax = plt.subplots(1, 2)
ax1, ax2 = ax.ravel()
ax1.imshow(BW_Original, cmap=plt.cm.gray)
ax1.set_title('Original binary image')
ax1.axis('off')

#print numpy.nonzero(im)
ax2.imshow(BW_Skeleton, cmap=plt.cm.gray)
ax2.set_title('Skeleton of the image')
ax2.axis('off')
plt.show()
"""

