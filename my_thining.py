#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Image, numpy
import sys
numpy.set_printoptions(threshold=numpy.nan)



im=numpy.asarray(Image.open('maze_black_white.jpg').convert('L'))
#print im
print im.shape
shape= im.shape
rows= shape[0]
cols=shape[1]
print rows
print cols

im.setflags(write=1)
for i in range(1,rows-1): 
   for j in range(1,cols-1):
	if im[i][j]!=255 and im[i-1][j]!=im[i+1][j] :
		im[i][j]=255
img = Image.fromarray(im)
img.show()
