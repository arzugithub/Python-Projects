'''
Exercise 10: 2D Rotation of a marix
Last update 14-June-2018
'''

from __future__ import division
from math import *
import math
import cmath
import numpy
import time
import numpy as np
import pylab as pl
import cv2


def swap (M, i1, j1, i2, j2):
  temp = M[i1][j1]
  M[i1][j1] = M[i2][j2]
  M[i2][j2] = temp
  return M

#print (swap(1,2)[0], swap(1,2)[1])   

A = [ [1,2,3], [4,5,6],[7,8,9] ]
#A = [ [1,2,3,4], [5,6,7,8],[9,10,11,12], [13,14,15,16],[17,18,19,20] ]
print ('Original A = ', A)
num_level = int(len(A)/2.0)
print ('num_level = ', num_level)
level = 0
last = len(A) - 1
num_r = len(A)  
num_c = len(A[0])  
print ('nimber of raws = ', num_r)
print ('number of columns = ', num_c)
#print (swap(A,0,0,0,1))
A_rot = [[None]*len(A) for i in range (0,len(A[0]))]
for i in range (0, num_r):
  for j in range (0, num_c):
    A_rot[j][num_r-1-i] = A[i][j]
print (A_rot)
  

'''
temp = A[0][0]
print ('temp = ', temp)
A[0][0] = A[0][1]
print ('A[0][0] = ', A[0][0])
A[0][1] = temp
print ('A[0][1] = ', A[0][1])
print (temp)
print (A)
'''
''' 
# 90 degree rotation by swapping
while level<num_level:
  for i in range (level, last):
    swap(A,level,i,i,last)
    swap(A,level,i,last,last-i+level)
    swap(A,level,i,last-i+level,level)
  level = level + 1
  last = last - 1
'''



    
