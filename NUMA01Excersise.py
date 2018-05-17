import numpy as np
import matplotlib.pyplot as plt


L=[1,2]
L3=3*L
L4=[k**2 for k in L3]

L5=L3+L4

L6=list(range(101))
L7=[x/100 for x in L6]

xplot=[]
for i in range(0,101):
    xplot.append(i/100)

yplot=[arctan(x) for x in xplot]

K=0
for i in range(1,201):
    K=K+(1/(sqrt(i)))

u=[1.0, exp((1/1000)*(-0.5)), exp(2*(1/1000)*(-0.5))]

a=0
b=0
c=0
ha=(1/1000)*(-0.5)
for i in range(0,998):
  a=(23/12)*float(u[i+2])
  b=(4/3)*float(u[i+1])
  c=(5/12)*float(u[i])
  u.append(u[i+2]+(ha*(a-b+c)))


td=[]
for i in range(0,1001):
    td.append(i*(1/1000))

dif=[]
i=0
for n in td:
    dif.append(abs(exp(-0.5*n)-u[i]))
    plt.plot(i,dif[i],'b.')
    #plt.plot(u[i],td[i], 'r.')
    plt.title('Difference of exp(at_n) and u_n')
    plt.xlabel('n')
    plt.ylabel('Difference')
    i=i+1
    


    
    
    
    
    
    
    
    