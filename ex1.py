'''
Exercise 1
Last update 28-May-2018
'''
from __future__ import division
from math import *
import cmath
import numpy
import time
import numpy as np
import pylab as pl
#start_time = time.time()

def f(x):
  val = x**2
  return val

def g():
  for i in range(0, 1000000):
    i = i + 1
  return None

def factorial(n):
  val = 1
  for i in range (2,n+1):
    val = val * i
  return val

def fact_rec(n):
  if n==1:
    val = 1  
  if n>1:
    val = n*fact_rec(n-1)
  return val  
  
n = input('Enter a number : ')
n = int(n)
# Hello World!
print()
print ('Hello World!')
print()

'''
# average
add = 0
n = 0
for i in range (0, 10):
  add = add + i
  n = n+1
print 'Summation = ', add
print 'Average = ', add/n
'''
'''
#factorial
fact = 1
for i in range (2, 6):
  fact = fact * i
print 'fact(6) = ', fact
'''
  
print (factorial(5) + factorial(8))

print (fact_rec(n))  



#end_time = time.time()
#print ('run_time = ', end_time - start_time, 's')

