'''
Image processing related: filtering spatial coordinates
Exercise 7
Last update 7-June-2018
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

def try_image(image):
  row,col,ch= image.shape
  print ('row = ', row)
  print ('column = ', col)
  print ('ch = ', ch)
  blue = img[120,180,0]
  print ('blue = ', blue)
  green = img[120,180,1]
  print ('green = ', green)
  red = img[120,180,2]
  print ('red = ', red)
  for i in range (65, 115):
    for j in range (175, 225):
      image[i,j] = [51,255,255]
  ball = img[100:150, 200:250] 
  img[50:100, 100:150] = ball
  for i in range (100, 150):
    for j in range (200, 250):
      image[i,j] = [255,255,255]
  return image


img = cv2.imread('2.jpg')
pl.imshow(img, cmap = 'gray', interpolation = 'bicubic')
pl.show()

