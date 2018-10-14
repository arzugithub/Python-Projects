'''
Matehmatical operations of matrices: addition and multiplication
Exercise 4
Last update 1-June-2018
'''
from __future__ import division
from math import *
import cmath
import numpy
import time
import numpy as np
import pylab as pl
start_time = time.time()


# Addition or substraction of two matrices
def add_2_mat (A,B):
  #val = [[0]*len(A[0]) for i in range(len(A))]   # or val = A
  if len(A)==len(B):
    for i in range (0, len(A)):
      if len(A[i]) == len(B[i]): 
        for k in range (0, len(A)):
          for j in range (0, len(A[i])):
            A [k][j] = A[k][j] + B[k][j]   # To substract: A [k][j] = A[k][j] - B[k][j]
        return A  
      else:
        print ('Beep! Two matrices must have the same dimension.')
  else:
    print ('Beep! Two matrices must have the same dimension.' ) 


def mul(D,E):
# iterating by row of D
  c = [[0 for row in range(len(E[0]))] for col in range(len(D))]
  c_num = len(D[0])
  
  for l in range(0,len(E[0])):

    # iterating by coloum by E 
    for k in range(0,len(D)):
 
        
        for i in range(0,c_num):
            c[l][k] = c[l][k] + D[l][i] * E [i][k]
          
              
  return c


a = [ [2,3,-1], [-4,0,5] ] # Define a specific 2*3 matrix  

# Call a list elements 
print ('a = ', a)
print ('a[0] =', a[0])
print ('a[1] =', a[1])
print ('a[0][1] =', a[0][1])
print ('a[1][0] =', a[1][0])

# Summation of all elements
add = 0
n = 0
for i in range (0, len(a)):
  for j in range (0, len(a[0])):
    print ('a[',i,',',j,'] = ',  a[i][j])
    add = add + a[i][j]
    n += 1     # i.e. n = n + 1 
print ('Summation = ', add)
print ('Average = ', add/n) #( len(a) * len(a[0]) ) # 2*len(a[0])

# List operations
b = [ [1,1,0], [2,-1,4] ]
d= [[1,2,3] , [4,5,6] ]
e=[[7,8], [9,10],[11,12]]
print ('a = ', a)
print ('b = ', b)
#c = a + b
#print ('a+b = ', c)    # merge two lists
#print 'len(c) = ', len(c)
#print 'a*b = ', a*b     # undefined

#val = [[0]*len(a[0]) for i in range(len(a))]
#print val

print ('a+b = ', add_2_mat(a,b))
print ('d*e =' , mul(d,e))

print (d[0][0]*e[0][0] + d[0][1]*e[1][0] + d[0][2]*e[2][0])




  
