# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 08:31:17 2016

@author: Martin Lindgren
"""

from scipy import *
from pylab import *
import numpy as np
from collections import Counter

E=[0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13]
GE=[18671059783.5,18671059783.5,5351538782,1222946058,234326487,
    40339545,5824861,710407,77535,9046,645,86,0,1]

epsilon=1
k=1
eMin=-13

T=linspace(0.1,1,1000)
C=[]

for i in range (1000):
    fnom=0
    fdenom=0
    fnom2=0
    fdenom2=0
    for j in range(14):
        fnom+=(E[j]**2)*GE[j]*e**(-(E[j]-eMin)/T[i])
        fdenom+=GE[j]*e**(-(E[j]-eMin)/T[i])
        fnom2+=E[j]*GE[j]*e**(-(E[j]-eMin)/T[i])
        fdenom2+=GE[j]*e**(-(E[j]-eMin)/T[i])
    f=fnom/fdenom
    f2=fnom2/fdenom2
    C.append((f-(f2**2))*(1/(T[i]**2)))
    

max_y = max(C)  # Find the maximum y value
max_x = T[C.index(max_y)]  # Find the x value corresponding to the maximum y value
print (max_x, max_y)
maxstr='Max value at x='+str(max_x)+'and y='+str(max_y)





monteCarlo1=np.genfromtxt('C:\\Users\\artin\\OneDrive\\Dokument\\Task3.1.csv', delimiter=',', names=['x','y'])

monteCarlo2=np.genfromtxt('C:\\Users\\artin\\OneDrive\\Dokument\\Task3.2.csv', delimiter=',', names=['x','y'])




eV1=0
for i in range(len(monteCarlo1)):
    eV1+=monteCarlo1['y'][i]
eV3=eV1
eV1=eV1/(len(monteCarlo1))

eV21=0
for i in range(len(monteCarlo1)):
    eV21+=monteCarlo1['y'][i]**2

eV21=(eV21)/(len(monteCarlo1))



eV2=0
for i in range(len(monteCarlo2)):
    eV2+=monteCarlo2['y'][i]

eV2=eV2/(len(monteCarlo2))

eV22=0
for i in range(len(monteCarlo2)):
    eV22+=monteCarlo2['y'][i]**2

eV22=(eV22)/(len(monteCarlo2))


cV1=((eV21-(eV1**2))/((0.9*max_x)**2))

cV2=((eV22-(eV2**2))/((1.1*max_x)**2))

b=figure(1)
plot(T,C,'b')
plot(max_x*0.9,cV1, 'ro')
plot(max_x*1.1,cV2, 'ko')
plt.axvline(x=max_x*0.9, color= 'r', ls='--')
plt.axvline(x=max_x*1.1, color= 'k', ls='--')
text(max_x*0.5, cV1, '0.9Tmax', color='r')
text(max_x*1.2, cV2, '1.1Tmax', color='k')
text(max_x, max_y, maxstr, color ='b')

P=[]

for i in range(1000):
    pnom=1
    pdenom=0
    for j in range(14):
        pdenom+=GE[j]*e**(-(E[j]-eMin)/(T[i]))
    P.append(pnom/pdenom)

   
    
c=figure(2)
plot(T,P,'b')

proc=P[list(T).index(max_x)]
#plot(max_x,proc, 'ro')

pN1=2252/len(monteCarlo1['y'])
pN2=1644/len(monteCarlo2['y'])

plot(max_x*0.9, pN1, 'ro')
plot(max_x*1.1, pN2, 'ko')
plt.axvline(x=max_x*0.9, color= 'r', ls='--')
plt.axvline(x=max_x*1.1, color= 'k', ls='--')
text(max_x*0.5, pN1, '0.9Tmax', color='r')
text(max_x*1.2, pN2, '1.1Tmax', color='k')


b.show()
c.show()
