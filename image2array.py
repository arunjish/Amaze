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

matrix = [[0 for x in range(700)] for y in range(700)]

#print type(rows)

for i in range(0,700): 
   for j in range(0,700):
	
	
	if i>rows-1 or j>cols-1:
		matrix[i][j]=5
		#sys.stdout.write(str(matrix[i][j]))
		#print i>rows or j>cols
	
	else:
		#print i>rows or j>cols
		
		if im[i][j]==0:
			#sys.stdout.write("%d " % im[num][i])
			matrix[i][j]=0
			#sys.stdout.write(str(matrix[i][j]))
		elif im[i][j]==1:
			#sys.stdout.write("1 ")
			matrix[i][j]=1
			#sys.stdout.write(str(matrix[i][j]))
		else:
			#sys.stdout.write("5 ")
			matrix[i][j]=5
			#sys.stdout.write(str(matrix[i][j]))
	
   #print "\n"


print len(matrix)	#rows of matrix
print len(matrix[0])	#columns of matrix



maize_reduced = [[0 for x in range(5)] for y in range(15)]

for i in xrange(0,700,7):
  for j in xrange(0,700,7):
	c_0=0
	c_1=0
	c_5=0
	for k in range(i,i+7):
		
		for l in range(j,j+7):
			#print "("+str(k)+","+str(l)+")"
			
			if matrix[k][l]==0:
				c_0 +=1
			elif matrix[k][l]==1:
				c_1+=1
			else:
				c_5+=1 
			
	d = {'.': c_0, '9': c_1, '#': c_5}
	#print str(c_0)+","+str(c_1)+","+str(c_5)+"-- "+max(d, key=d.get)
	big = 	max(d,key=d.get)
	#maize_reduced[i%10][j%10]=big
	#print maize_reduced
	#print j%10
	sys.stdout.write(str(big))
  sys.stdout.write("\n") 
#print matrix



