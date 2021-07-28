#Python code for 5a)

from numpy import linspace, arange
from math import exp
import matplotlib.pyplot as plt

R = 40
#N = 64
N = 128
x0 = 0
xN = 1
dx = 1/N
t0 = 0
tf = 10
#dt = 0.005
dt = 0.00125

x = linspace(x0,xN,N+1)
t = arange(t0,tf+dt,dt)

def f(x):
    return 1 - x

def usoln(x):
    return (exp(R) - exp(R*x))/(exp(R) - 1)

nu = dt/dx
mu = dt/(R*dx**2)

u0 = []

for j in range(0,N+1):
    u0.append(f(x[j]))

u = u0

for tn in t:
    u[0] = 1
    u[N] = 0
    for j in range(1,N):
        u[j] = u0[j] - nu*(u0[j] - u0[j-1]) + mu*(u0[j+1] - 2*u0[j] + u0[j-1])
    u0 = u

u_ex = []

for xj in x:
    u_ex.append(usoln(xj))

plt.plot(x,u_ex,label="Exact soln")
plt.plot(x,u,label=r"Numerical soln w/ N = ${}$".format(N))
plt.title(r"Solution for u(x,t) @ t=10 w/ $\Delta$t = ${}$".format(dt))
plt.xlabel("x")
plt.ylabel("u(x)")
plt.legend(loc="best")
plt.show()

E = []

for j in range(0,len(x)):
    err = abs(u[j] - u_ex[j])
    E.append(err)

print(max(E))