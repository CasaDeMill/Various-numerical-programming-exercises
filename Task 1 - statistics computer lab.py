# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 22:23:59 2016

@author: artin
"""
from scipy import *
from pylab import *
import sys

N=[20,40,80,160]
r2=[66.7,193,549,1555]

k=((log(r2[-1]/r2[0]))/(log(N[-1]/N[0])))/2


loglog(r2,N)



print(k)