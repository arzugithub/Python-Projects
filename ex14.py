p'''
Exercise 13: Monte Carlo estimaion of PI
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
import random

# Definition of circle function
def c(x):
  val = sqrt(1-x**2)
  return val
#total = 10000


# add a loop to do update proccess of MC n times and find the average
for total in range (0,50):
  target = 0
  for i in range(0, total):
    X = random.random()
    Y = random.random()
    if Y <= c(X):
      target = target + 1

print ('MC estimation = ', target/total)
print ('Exact result = ', math.pi/4)
