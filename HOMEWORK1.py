# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 22:19:49 2016

@author: artin
"""
from scipy import *
from pylab import *
import sys
#The first row is only to make plots from matplotlib inline in the file. That so the code can be presented better. 
#I also import the matplotlib package using pylab.
#The second line is importing the scipy library, which will be used many times in this homework. I import it as *
#which means that i don't have to write anything before using something from the library

#I define a function that takes 4 arguments. f,a,b and n.
def ctrapezoidal(f,a,b,n):
    
    #I set a variale I and h to 0. I will be used to calculate the sum of the trapezoidal areas
    I=0
    h=0
    
    #I loop n-1 times
    for i in range(n-1):
        #I calculate x and h according to the background theory
        x=a+((i/n)*(b-a))
        h=((b-a)/n)
        
        #I represents the sum symbol in the equation. It adds the last value of I in every loop.
        I=I+(h*f(x))
        
        #I then return the sum plus (h/2*(f(a)+f(b))) to complete the formula
    return I+(h/2)*(f(a)+f(b))

#Here i call the function with the f(x)=2x+4x^2 and calculate the integral on the interval 3 to 4 with 1000 trapezoids
ctrapezoidal(lambda x: 2*x+4*x**2, 3, 4, 1000)

#I first declare the variable error to zero and then tolerance to something very small to try
error=0
tolerance=0.0001

#I make a long loop to make sure the error becomes small enough before the loop is done. Ideally I would like to
#use a while loop, but I could not get it working.
for n in range(1,10000):
   
    #Here I calculate the error between two adjacent values using the function I previously wrote. 
    error=abs(ctrapezoidal(lambda x: 2*x+4*x**2,3,4,n) - ctrapezoidal(lambda x: 2*x+4*x**2,3,4,n+1))
    
    #I break the loop if the error is less than my tolerance
    if error<tolerance:
        break

#I print out the number of loops it took before the error became small enough and print out that error.
print(n)
print(error)

#I start with the same method as in the previous task. I also set a and b since they will be used later to calculate h 
#and writing the same number several times is unnecessary.
error=0
tolerance=0.0001
a=3
b=4

for n in range(1,1000):
    error=abs(ctrapezoidal(lambda x: 2*x+4*x**2,a,b,n) - ctrapezoidal(lambda x: 2*x+4*x**2,a,b,n+1))
    
    #I calculate h
    h=((b-a)/n)
    
    #I plot in double logarithmic scale. With blue dots as markers
    #loglog(h,error,'b.')
    
    #I turn on the plot grid
    grid()
    
    
#I define a function I call matrixconstructor. It takes the argument x 
def matrixconstructor(x):
    
    #Here I remove the value on the last index of the vector. So the matrix can be N rows and N columns 
    #The vector then has the lenght (N+1)
    reducedx=x[:-1]
    
    #I make a list in where I store my arrays
    arrays=[]
    
    #I loop the lenght of x -1 times (N times)
    for n in range(len(x)-1):
        #I append the reduced array to the power of n. This happens elementwise
        arrays.append(reducedx**(n))
   
    #I make a matrix with the arrays in my list stacked in columns. I also flip the vectors around to match the
    #matrix in the theroy
    matrix=fliplr(column_stack(arrays))
    
    #I return the matrix
    return matrix

#Here I declare an array and use my newly written function on it. I print the results to check. I overwrite my x so
#after the function is used x now has the length (N)
x=array([1,2,3,4])
x=matrixconstructor(x)
print(x)

#I define a function called interpoly which takes the arguments x and y
def interpoly(x,y):
    
    #First, I remove the last index of the y array to make sure it has the lenght (N)
    reducedy=y[:-1]
    
    #I use the solve function to solve xc=reducedy for c
    
    c=solve(x,reducedy)
    
    #I return c
    return c

#I declare an array y, apply my function and print out the result
y=array([1,2,3,4])
c=interpoly(x,y)
print(c)

#I define a function called polyval that takes the arguments c and z
def polyval(c,z):
    
    #I set P to 0. Similar to how I used I in task 1. It will be used to calculate the sum
    P=0
    
    #I loop the lenght of c number of times
    for i in range(len(c)):
        
        #I computer the polynomial according to the theory
        P=P+(c[i]*(z**i))
    
    #Then I return P
    return P

#I try it out with a value z which i declare to 3 
z=3
polyval(c,z)

#First I turn on the grid and declare my 2 vectors. I name the x3 and y3 just so I won't be confused
grid()
axis([-1,4,-3,3])
x3=array([0.0,0.5,1.0,1.5,2.0,2.5])
y3=array([-2.0,0.5,-2.0,1.0,-0.5,1.0])

#I then plot the values by looping the length of x3 times (also the length of y3).
for i in range(len(x3)):
    #I plot the values of x3 and y3 on position i with a red star.
    plot(x3[i],y3[i],'r*')

#I use my matrixconstructor to represent my vectors as a matrix according to the theory
x3=matrixconstructor(x3)

#I then use my interpoly function to calculate the coefficient matrix
c3=interpoly(x3,y3)

#I loop 300 times
for n in range(0,301):
    #I plot n/100 vs the polyvalue of c3 and n/100 so the polynomial will go from index 0 to 3. I do so with a blue dot.
    plot((n/100),polyval(c3,(n/100)),'b.')