# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 11:19:14 2017

@author: artin
"""
from scipy import *
from pylab import *
import sys

# Parameters
xmin=-8
xmax=-xmin
Nsteps=1001
alpha=1.0
V0=4.0

x=linspace(xmin,xmax,Nsteps+1)
y=linspace(0,0,Nsteps+1)
h=x[1]-x[0]
V=-V0*(e**((-1)*(alpha*(x**2))))

E=-2.774494764

k=sqrt(-2*E)
y[0]=1
y[1]=e**(k*h)

a=[]
b=[]

for i in range(Nsteps):
    a.append((2+((10*(h**2)*2*(V[i]-E))/(12)))/(1-(((h**2)*2*(V[i+1]-E))/(12))))
    b.append((-1)*((1-(((h**2)*2*(V[i-1]-E))/(12)))/(1-(((h**2)*2*(V[i+1]-E))/(12)))))
    
for i in range(Nsteps):
    y[i+1]=a[i]*y[i]+b[i]*y[i-1]
plot(x,y)
show()

