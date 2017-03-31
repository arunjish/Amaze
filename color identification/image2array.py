#!/usr/bin/ python
# -*- coding: utf-8 -*-

import numpy
import sys
from PIL import Image
numpy.set_printoptions(threshold=numpy.nan)





image=Image.open('poops.jpg')
im=numpy.asarray(image)

shape= im.shape
rows= shape[0]
cols=shape[1]
print rows
print cols
'''
listall=[[255,255,255],[254,254,254],[252,252,252],[251,251,251],[231,231,231]]

print type(list)
print list

ndList= numpy.array(list)
print type(ndList)
print ndList


listRed=[[255,0,0],[0,255,0]]

print type(listRed)
print listRed

ndListRed= numpy.array(listRed)
print type(ndListRed)
print ndListRed
'''

redCordinates=[]

for i in range(rows-1,0,-1): 
	for j in range(cols-1,0,-1):
		if im[i][j][0]==255 and im[i][j][1] in range(0,50) and im[i][j][2] in range(0,50)  : 
			sys.stdout.write("red : "+ str(im[i][j]) +"("+str(i)+","+str(j)+")" + "\n ")
			redCordinates.append((i,j))
print redCordinates
"""
for i in range(0,rows): 
	for j in range(0,cols):
		if im[i][j][0] in range(0,50) and im[i][j][1] in range(200,256) and im[i][j][2] in range(0,50)  : 
			sys.stdout.write("green : "+str(im[i][j])+ "\n ")
	#sys.stdout.write("\n")

"""
