# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 21:56:25 2017

@author: artin
"""
from scipy import *
from pylab import *
import sys

# Parameters
M=526
Etol=10**(-8)
xmin=-16
xmax=-xmin
Nsteps=1001
alpha=1.0
V0=4.0

x=linspace(xmin,xmax,Nsteps+1)
xM=x[52]
y=linspace(0,0,Nsteps+1)
h=x[1]-x[0]
V=-V0*(e**((-1)*(alpha*(x**2))))

yL=linspace(0,0,Nsteps+1)
yR=linspace(0,0,Nsteps+1)

E=-2.7744948100000317
deltaE=1

while (abs(deltaE) > Etol):
   a=[]
   b=[]

   k=sqrt(-2*E)
   yL[0]=1
   yL[1]=e**(k*h)
   yR[Nsteps-1]=1
   yR[Nsteps-2]=e**(k*h)
  

   for i in range(Nsteps):
       a.append((2+((10*(h**2)*2*(V[i]-E))/(12)))/(1-(((h**2)*2*(V[i+1]-E))/(12))))
       b.append((-1)*((1-(((h**2)*2*(V[i-1]-E))/(12)))/(1-(((h**2)*2*(V[i+1]-E))/(12)))))
   for i in range(1, M+2):
       yL[i+1]=a[i]*yL[i]+b[i]*yL[i-1]
   for i in reversed(range(M-2, Nsteps)):
       yR[i-1]=(1/b[i])*yR[i+1]-(a[i]/b[i])*yR[i]
       

   ydL=(1/(12*h))*(yL[M-2]-8*yL[M-1]+8*yL[M+1]-yL[M+2])
   ydR=(1/(12*h))*(yR[M-2]-8*yR[M-1]+8*yR[M+1]-yR[M+2])
   yDL=M*(ydL/yL[M])
   yDR=M*(ydR/yR[M])
   sumL=0
   sumR=0
   for i in range(1,M):
       sumL+=yL[i]**2
   for i in range(M+1,Nsteps):
       sumR+=yR[i]**2
   integL=h*((yL[0]/2)+sumL+(yL[M]/2))
   integR=h*((yR[M]/2)+sumR+(yR[Nsteps]/2))
   yLdE=(-1)*((2*M)/(yL[M]**2))*integL
   yRdE=((2*M)/(yR[M]**2))*integR
   
   deltaE=-((yDL-yDR)/(yLdE-yRdE))
   E+=0.00000001
   print(E)
   print(deltaE)
   
plot(x,yL)
plot(x,yR)
print(deltaE)
show()