# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 12:02:45 2016

@author: artin
"""
from scipy import *
from scipy.optimize import fsolve
from pylab import *
import sys

hbar=6.58212*(10**-16)
omega1=3.07999*(10**15)
omega2=2.71607*(10**15)
omega3=2.61074*(10**15)
omega4=2.22282*(10**15)
eGaAs=1.52
v0=0.44
mestar=1.14123*(10**-12)
mhstar=8.17598*(10**-12)
L1=0.72*(10**-9)
L2=1.4*(10**-9)
L3=2*(10**-9)
L4=3.5*(10**-9)


intersectE1=0
intersectH1=0
intersectE2=0
intersectH2=0
intersectE3=0
intersectH3=0
intersectE4=0
intersectH4=0

leftSide1=abs((hbar*omega1)-eGaAs)
leftSide2=abs((hbar*omega2)-eGaAs)
leftSide3=abs((hbar*omega3)-eGaAs)
leftSide4=abs((hbar*omega4)-eGaAs)


ae1=tan((L1/2)*sqrt(0.0001*((2*mestar)/(hbar**2)))) 
ah1=tan((L1/2)*sqrt(0.0001*((2*mhstar)/(hbar**2)))) 
be1=sqrt((v0-0.0001)/0.0001)
ae2=tan((L1/2)*sqrt(0.0001*((2*mestar)/(hbar**2)))) 
ah2=tan((L1/2)*sqrt(0.0001*((2*mhstar)/(hbar**2)))) 
be2=sqrt((v0-0.0001)/0.0001)
ae3=tan((L1/2)*sqrt(0.0001*((2*mestar)/(hbar**2)))) 
ah3=tan((L1/2)*sqrt(0.0001*((2*mhstar)/(hbar**2)))) 
be3=sqrt((v0-0.0001)/0.0001)
ae4=tan((L1/2)*sqrt(0.0001*((2*mestar)/(hbar**2)))) 
ah4=tan((L1/2)*sqrt(0.0001*((2*mhstar)/(hbar**2)))) 
be4=sqrt((v0-0.0001)/0.0001)


E=linspace(0,0.5,100)
tol=0.00285

eE1=0
eH1=0
while (abs(leftSide1-(eE1+eH1)) > tol):
    eE1=0
    eH1=0
    intersectListE1=[]
    intersectListH1=[]
    AE1=[]
    AH1=[]
    BE1=[]
    L1+=0.001*(10**-9)
    for i in range(100):
        ae1=tan((L1/2)*sqrt(E[i]*((2*mestar)/(hbar**2)))) 
        ah1=tan((L1/2)*sqrt(E[i]*((2*mhstar)/(hbar**2)))) 
        be1=sqrt((v0-E[i])/E[i])
        AE1.append(ae1)
        AH1.append(ah1)
        BE1.append(be1)
        intersectListE1=np.argwhere(np.isclose(array(AE1),array(BE1), atol=0.01)).reshape(-1)
        intersectListH1=np.argwhere(np.isclose(array(AH1),array(BE1), atol=0.01)).reshape(-1)
        if intersectListE1.any():
            eE1=E[intersectListE1[0]]
        if intersectListH1.any():
            eH1=E[intersectListH1[0]]
    print(L1)
        
print('L1 is: ' + str(L1))
a=figure(1)    
plot(E,AE1, 'k')
plot(E,AH1,'r')
plot(E,BE1,'b')
ylim([0,1.5])
xlim([0,0.5])

eE2=0
eH2=0
while (abs(leftSide2-(eE2+eH2)) > tol):
    eE2=0
    eH2=0
    intersectListE2=[]
    intersectListH2=[]
    AE2=[]
    AH2=[]
    BE2=[]
    L2+=0.001*(10**-9)
    for i in range(100):
        ae2=tan((L2/2)*sqrt(E[i]*((2*mestar)/(hbar**2)))) 
        ah2=tan((L2/2)*sqrt(E[i]*((2*mhstar)/(hbar**2)))) 
        be2=sqrt((v0-E[i])/E[i])
        AE2.append(ae2)
        AH2.append(ah2)
        BE2.append(be2)
        intersectListE2=np.argwhere(np.isclose(array(AE2),array(BE2), atol=0.1)).reshape(-1)
        intersectListH2=np.argwhere(np.isclose(array(AH2),array(BE2), atol=0.1)).reshape(-1)
        if intersectListE2.any():
            eE2=E[intersectListE2[0]]
        if intersectListH2.any():
            eH2=E[intersectListH2[0]]
   
    print(L2)
        
print('L2 is: ' + str(L2))
b=figure(2)    
plot(E,AE2, 'k')
plot(E,AH2,'r')
plot(E,BE2,'b')
axis([0,0.3,0,3])

eE3=0
eH3=0
while (abs(leftSide3-(eE3+eH3)) > tol):
    eE3=0
    eH3=0
    intersectListE3=[]
    intersectListH3=[]
    AE3=[]
    AH3=[]
    BE3=[]
    L3+=0.001*(10**-9)
    for i in range(100):
        ae3=tan((L3/2)*sqrt(E[i]*((2*mestar)/(hbar**2)))) 
        ah3=tan((L3/2)*sqrt(E[i]*((2*mhstar)/(hbar**2)))) 
        be3=sqrt((v0-E[i])/E[i])
        AE3.append(ae3)
        AH3.append(ah3)
        BE3.append(be3)
        intersectListE3=np.argwhere(np.isclose(array(AE3),array(BE3), atol=0.011)).reshape(-1)
        intersectListH3=np.argwhere(np.isclose(array(AH3),array(BE3), atol=0.035)).reshape(-1)
        if intersectListE3.any():
            eE3=E[intersectListE3[0]]
        if intersectListH3.any():
            eH3=E[intersectListH3[0]]
        
    print(L3)
print('L3 is: ' + str(L3))
c=figure(3)    
plot(E,AE3, 'k')
plot(E,AH3,'r')
plot(E,BE3,'b')
axis([0,0.2,0,4])

eE4=0
eH4=0
while (abs(leftSide4-(eE4+eH4)) > tol):
    eE4=0
    eH4=0
    intersectListE4=[]
    intersectListH4=[]
    AE4=[]
    AH4=[]
    BE4=[]
    L4+=0.01*(10**-9)
    for i in range(100):
        ae4=tan((L4/2)*sqrt(E[i]*((2*mestar)/(hbar**2)))) 
        ah4=tan((L4/2)*sqrt(E[i]*((2*mhstar)/(hbar**2)))) 
        be4=sqrt((v0-E[i])/E[i])
        AE4.append(ae4)
        AH4.append(ah4)
        BE4.append(be4)
        intersectListE4=np.argwhere(np.isclose(array(AE4),array(BE4), atol=0.015)).reshape(-1)
        intersectListH4=np.argwhere(np.isclose(array(AH4),array(BE4), atol=0.015)).reshape(-1)
        if intersectListE4.any():
            eE4=E[intersectListE4[0]]
        if intersectListH4.any():
            eH4=E[intersectListH4[0]]
    print(L4)
    print(abs(leftSide4-(eE4+eH4)))
        
print('L4 is: ' + str(L4))
d=figure(4) 
plot(E,AE4, 'k')
plot(E,AH4,'r')
plot(E,BE4,'b')
axis([0,0.07,0,7])

a.show()
b.show()
c.show()
d.show()