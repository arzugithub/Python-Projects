'''
Mean filter on an image
Exercise 8
Last update 11-June-2018
'''

from __future__ import division
from math import *
import cmath
import numpy
import time
import numpy as np
import pylab as pl
import cv2
start_time = time.time()

img = cv2.imread('2.jpg')
row,col,ch= img.shape

#print img   # to print all the pixels of image
pl.imshow(img, cmap = 'gray', interpolation = 'bicubic')
pl.show()

#cv2.waitKey(0)
#cv2.destroyAllWindows()

avg = 0
count = 0
for i in range (0, row):   # Mean Green Filter
  for j in range (0, col):
    avg = avg + img[i,j][1]     
    count = count + 1
avg = avg/count
for i in range (0, row):
  for j in range (0, col):
    img[i,j][1] = avg



cv2.imshow('image2',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
