# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 09:07:08 2016

@author: artin
"""
from scipy import *
from pylab import *
import sys

x=0.5
a=0.5
z=31
L=linspace(5,30, num=26)
print(L)
for i in range(5,z):
    x=sin(x)-a*x+30
    plot(x,L[i-5],'b.')
    plot(x,L[i-5])
    if abs((x**(i+1))-(x**i)) < 1.e-8:
        print('The result after {num} iterations is {res}'.format(num=i+1, res=x))
        break
    else:
        if i == z-1:
            print('The condition was not met after {num} iteration steps'.format(num=i+1))
            break
        

        
