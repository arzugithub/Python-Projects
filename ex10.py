'''
Exercise 10: 2D Rotation
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

def Rot(ANG, P):
  val = [ 0, 0 ]
  R_z = [ [cos(ANG), sin(ANG)], [-sin(ANG), cos(ANG)] ]  
  val[0] = R_z[0][0]*P[0] + R_z[0][1]*P[1]
  val[1] = R_z[1][0]*P[0] + R_z[1][1]*P[1]
  return val


# Variables: Begin {
ang = math.pi/2.0
x = 0.0
y = 1.0 
r = [ x, y ]
print ('ang = ', ang)
print ('r = ', r)
#print 'r[0] = ', r[0]
#print 'r[1] = ', r[1]
#R_z = [ [cos(ang), sin(ang)], [-sin(ang), cos(ang)] ]
#print 'R_z = ', R_z 
#r_new = [ 0, 0 ]
# Variables: End }


# Apply rotation: Begin {
#r_new[0] = R_z[0][0]*r[0] + R_z[0][1]*r[1]
#r_new[1] = R_z[1][0]*r[0] + R_z[1][1]*r[1]
#print 'r_new = ', r_new 
# Apply rotation: End }    

print ('r_new = ', Rot(ang, r))
