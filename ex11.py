'''
Exercise 11: 2D Rotation for a set of data
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
start_time = time.time()

def AVG(d_win, init_mat):
  d_init = len(init_mat)
  for s_i in range (0, d_init-d_win+1):  # To sweep along i axis
    for s_j in range (0, d_init-d_win+1): # To sweep along j axis
      avg = 0
      #s_i = 2
      #s_j = 1
      for i in range (s_i,d_win+s_i):
        for j in range(s_j,d_win+s_j):
          #print (i, ' ' , j)   # check indices
          avg = avg + init_mat[j][i]  # j is raw number and i is column number   
      avg = avg/l**2
      #print ( 'avg = ', avg)
      init_mat[s_j+1][s_i+1] = avg
  return init_mat   

#A = [ [1,2,3,4,5,6], [7,-1,9,10,11,12], [13,14,15,16,17,18], [19,20,21,22,23,24], [25,26,27,28,29,30], [31,32,33,34,35,36]] # initial configuration
#print ('A = ', A)
#N = len(A)
#print ('len(A) = ', N)
l = input('enter dimension of the window ')
l = int(l)
N = input('enter dimension of the initial matrix ')
N = int(N)
A = [ [None]*N for i in range (0,N) ]
print (A)
for i in range (0, N):
  for j in range(0, N):
    print ('A[',i,',',j, '] = ')
    A[i][j] = int(input())

'''
for s_i in range (0, N-l+1):
  for s_j in range (0, N-l+1):
    avg = 0
    #s_i = 2
    #s_j = 1
    for i in range (s_i,l+s_i):
      for j in range(s_j,l+s_j):
        #print (i, ' ' , j)   # check indices
        avg = avg + A[j][i]  # j is raw number and i is column number   
    avg = avg/l**2
#print ( 'avg = ', avg)
    A[s_j+1][s_i+1] = avg
'''
print ('A_updated =', AVG(l,A))

