'''
Exercise 3
Last update 30-May-2018
'''
from __future__ import division
from math import *
import cmath
import numpy
import time
import numpy as np
import pylab as pl
start_time = time.time()

# To perform the dot product between two 3D vectors 
def dot_prod(a,b):
  val = a[0]*b[0] + a[1]*b[1] + a[2]*b[2]
  return val




# To perform cross product
def cross_prod(a,b):
  val_cross=[ a[1]*b[2] -a[2]*b[1],
             -a[0]*b[2]+a[2]*b[0],
             a[0]*b[1]+a[1]*b[0]]
  return val_cross

temp=0

# To perform the dot product between two 3D vectors with for loop
def dot_prod4(a,b):
  val=0 #local value
  for i in range (len(a)):
    val = val +a[i]*b[i]
    
    
  return val


mat = [1,-2, 13, 94]   # Definition of a list


for i in range (0,4):
  print ('mat [', i, '] = ', mat[i])

print ('length mat = ', len(mat))  # len(list) returns the length of the list

#print mat[3] 

tot = 0.0
for i in range (0, len(mat)):
  tot = tot + mat[i]
avg = tot/len(mat)

print ('Average = ', avg)

# Call dot_prod
Amir = [1, 2, -1]
Arzu = [4, 0, 10]
print ('Amir.Arzu = ', dot_prod4(Arzu, Amir)) 

# Call cross_prod
A = [1, 2, -1]
B = [4, 0, 10]
print ('A*B = ', cross_prod(A,B)) 


print (mat)

#Definition of a list with an arbitrary lengthlength 
A = [0]*10
print (A)
