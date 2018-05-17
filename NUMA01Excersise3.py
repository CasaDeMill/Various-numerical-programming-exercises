# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 08:59:01 2016

@author: artin
"""
from scipy import *
from pylab import *
import sys

L=[0,1,2,1,0,-1,-2,-1,0]

def f(x):
    return sin(x)
    
def f(m):
    L=[n-m/2 for n in range(m)]
    return 1 +L[0] + [L-1]