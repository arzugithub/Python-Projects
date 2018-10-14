'''
Exercise 15: Fibbo series generation and save result in a txt file
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

#Fibb. sequence
a1 = 1
a2 = 1
file = open('Fibb.dat', 'w')
txt = str(a1) + '\n'
file.write(txt)
txt = str(a2) + '\n'
file.write(txt)

#file = open('Fibb.dat', 'w')
#txt1 = str(a1) + '\t' + str(a2) + '\n'
#file.write(txt1)
#print(a1, end='\t', flush=True)
#print(a2, end='\t', flush=True)



for i in range (0,50):
  
  # print (a1+a2, '\t')
  # print(a1+a2, end='\t', flush=True)
  
   a1_old = a1
   a2_old = a2
   a1 = a2_old
   a2 = a1_old+a2_old
   txt = str(a2) + '\n'
   file.write(txt)

   print(a2/a1, end='\t', flush=True)
   #txt = str(a2_old) + '\t' + str(a2) + '\n'
   #file.write(txt)
file.close()



   

  
 # file = open('Fibb2.dat', 'w')
  #txt2 = str(a1/a2) + '\t' '\n'
  #file.write(txt2)
 

