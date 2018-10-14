'''
Plot a function and its first order derivative 
Exercise 5
Last update 2-June-2018
'''

from __future__ import division
from math import *
import cmath
import numpy
import time
import numpy as np
import pylab as pl
start_time = time.time()

def g(arg):
  val = sin(arg)   # Arbitrary function
  return val

def der_1st(x,h):
  val = (g(x+h)-g(x))/h
  return val

H = 0.0001
pi = 3.1415926535897932384626433
'''
X = input('Enter the argument of the function:')
print 'sin( ',X,') = ', g(X)
print 'der_sin(',X,') = ', der_1st(X,H)
'''

file = open('g_plot.dat', 'w')
n = 100
a = -pi
b = pi
delta = (b-a)/n
for i in range (0, n+1): 
  X = a + i*delta
  Y = g(X)
  txt = str(X) + '\t' + str(Y) + '\n'
  file.write(txt)
file.close()
file = open('der_g_plot.dat', 'w')
for i in range (0, n+1): 
  X = a + i*delta
  Y = der_1st(X, H)
  txt = str(X) + '\t' + str(Y) + '\n'
  file.write(txt)
file.close()

data1 = np.loadtxt('g_plot.dat')
data2 = np.loadtxt('der_g_plot.dat')
pl.title(r'$y = \sin (x)$')
pl.xlabel(r'$x$', fontsize=25)
pl.ylabel(r'$y$', fontsize=25)
pl.xlim([-4,4])
pl.ylim([-2,2])
pl.plot(data1[:,0], data1[:,1], label=r'$\sinx$')     # we draw the g(x) plot: plot second column vs. first column, e.g. data[:,0] is X and data[:,1] is Y.
pl.plot(data2[:,0], data2[:,1], label=r'$\cosx$')
pl.legend(loc='best')
pl.savefig('g_plot.eps', format='eps', dpi=1200)  # To save the figure
pl.show() # To show the figure

  

