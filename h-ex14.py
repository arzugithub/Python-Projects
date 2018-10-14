'''
Exercise 14: Monte Calo estimation of PI and convergence issue
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
total = 10000
Avg=0

file = open('MC.dat', 'w')
# add a loop to do update proccess of MC n times and find the average
for loop in range (0,5):
  target = 0
  for i in range(0, total):
    X = random.random()
    Y = random.random()
    if Y <= c(X):
      target = target + 1
  
  txt = str(loop) + '\t' + str(target/total) + '\n'
  #txt = str(target/total) + '\n'
  file.write(txt) 
  Avg=Avg+target/total
  #print ('MC estimation = ', target/total)
  #print ('Exact result = ', math.pi/4)
 # MC estimation = (target/total)
  #print ('Avg = ', MC estimation /5)
file.close()

print ('Avg = ', Avg /5)
print ('Exact result = ', math.pi/4)

data = np.loadtxt('MC.dat')
pl.title(r'$\int \sqrt{1-x^2}dx$')
pl.xlabel(r'$loop$', fontsize=10)
pl.ylabel(r'$Integral$', fontsize=10)

pl.plot(data[:,0], data[:,1], label=r'$g(x)=\sqrt(1-x**2)}$')  #0 for x 1 foy y   

pl.savefig('MC', format='eps', dpi=1200)  # To save the figure
pl.show() # To show the figure




