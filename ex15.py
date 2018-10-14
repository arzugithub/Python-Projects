'''
Exercise 15: For exercise
Last update 24-June-2018
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

'''
# Index game
for i in range (0,5):
  for j in range (i,8):
    print ('i = ', i, 'j= ', j)
'''

#Fibb. sequence
a1 = 1
a2 = 1
file = open('Fibb.dat', 'w')
txt1 = str(a1) + '\t' + str(a2) + '\n'
file.write(txt1)
print(a1, end='\t', flush=True)
print(a2, end='\t', flush=True)



for i in range (0,50):
   #print (a1+a2, '\t')
   #print(a1+a2, end='\t', flush=True)

   a1_old = a1
   a2_old = a2
   a1 = a2_old
   a2 = a1_old+a2_old

   print(a2/a1, end='\t', flush=True)
 

'''
# Stars war
for i in range(0,5): # For raws
  for j in range(0,i+1): # To print stars
    print('*', end=' ', flush=True) 
  print()

for i in range (0,4):
  for j in range(0,-i+3):
    print(' ', end=' ', flush=True)
  for j in range(0,2*i+1):
    print('*', end=' ', flush=True)
  print()
'''
'''
name = 'A_'
for i in range (1,11):
  name_full = name + str(i)
  file = open(name_full,'w')
  for j in range (0,i):
    txt = '*' + '\n'
    file.write(txt)
  file.close()

for i in range(1,11):
  name_full = name + str(i)
  file = open(name_full,'r')
  print (file.read())
'''
