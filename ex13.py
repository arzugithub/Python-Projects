'''
Exercise 13: 1D Riemann integral
Last update 23-June-2018
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


# Definition of integrand
def f(X):
  val = X**2
  return val

a = 1.0
b = 3.0
n = 10000
t=10000

integral = 0
step = 10
num_steps = 100
file = open('Riemann.dat', 'w')
for j in range(1,num_steps+1):  # For steps with some arbitrary length
  for i in range (0, step*j): # To change n with a specific step 
    delta_x = (b-a)/(step*j)
    integral = integral + f(a+(i-1)*delta_x)*delta_x
  txt = str(step*j) + '\t' + str(integral) + '\n'
  file.write(txt)
  integral = 0
file.close()
#print ('For n = ', n , ' integral is equal to', integral)  
#print ('Exact result is ', (b**3-a**3)/3.0)  

 



data = np.loadtxt('Riemann.dat')
pl.title(r'$\int _1 ^3 X**2 dX$')
pl.xlabel(r'$n$', fontsize=1)
pl.ylabel(r'$Integral$', fontsize=3)
#pl.xlim([-4,4])
#pl.ylim([-2,2])
pl.plot(data[:,0], data[:,1], label=r'$g(x)=\X**2}$')  #0 for x 1 foy y   

pl.savefig('Riemann', format='eps', dpi=1200)  # To save the figure
pl.show() # To show the figure



