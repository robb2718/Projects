#python code
from numpy import arange, array, sqrt
import matplotlib.pyplot as plt

N = 625
dt = 10/N
tpoints = arange(0,10,dt)

y0 = array([1,1,1,1],float)

def f(y):
    y_0 = y[0]
    y_1 = y[1]
    y_2 = y[2]
    y_3 = y[3]
    f0 = 10*y_1 - 20*y_0
    f1 = 10*y_0 - 20*y_1 + 10*y_2
    f2 = 10*y_1 - 20*y_2 + 10*y_3
    f3 = 10*y_2 - 20*y_3
    return array([f0,f1,f2,f3],float)

y1 = y0 + dt*f(y0)
y2 = y1 + dt*f(y1)

#Euler method

ynorm = []

def eclnorm(x1,x2,x3,x4):
    xr = sqrt(x1**2 + x2**2 + x3**2 + x4**2)
    return xr


for t in tpoints:
    if t == 0:
        yi = y0
    if t == dt:
        yi = y1
    if t == 2*dt:
        yi = y2
    
    if t > 2*dt:
        yi = y2 + dt*(23*f(y2) - 16*f(y1) + 5*f(y0))/12
        #Adams-Bashforth method
        y0 = y1
        y1 = y2
        y2 = yi
    
    yn = eclnorm(yi[0],yi[1],yi[2],yi[3])
    ynorm.append(yn)

plt.plot(tpoints,ynorm,label=r"N = {}".format(N))
plt.xlabel('t')
plt.ylabel('ynorm')
plt.title("Numerical soln to y'=Ay")
plt.legend(loc='best')
plt.show()
