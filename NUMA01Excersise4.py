# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 13:47:57 2016

@author: artin
"""
from scipy import *
from pylab import *
import sys

def f(x,y):
    return y*exp(1j*x)
    
    
Lx=linspace(0,2*pi, 100)
Ly=linspace(0.1,1,100)

for i in range (100):
    plot(Lx[i],0.1,'b.')
for i in range (100):
    plot(Lx[i],0.2,'b.')
for i in range (100):
    plot(Lx[i],0.3,'b.')
for i in range (100):
    plot(Lx[i],0.4,'b.')
for i in range (100):
    plot(Lx[i],0.5,'b.')
for i in range (100):
    plot(Lx[i],0.6,'b.')
for i in range (100):
    plot(Lx[i],0.7,'b.')
for i in range (100):
    plot(Lx[i],0.8,'b.')
for i in range (100):
    plot(Lx[i],0.9,'b.')
for i in range (100):
    plot(Lx[i],1,'b.')


            
