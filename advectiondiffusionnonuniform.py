#Python code for 5b

from numpy import arange
from math import exp, log
import matplotlib.pyplot as plt

R = 40
N = 64
#N = 128
c = (2/R)*log(N)
t0 = 0
tf = 10
dt = 0.001
#dt = 0.00025

t = arange(t0,tf,dt)

x = []

dx1 = 2*(1 - c)/N
dx2 = 2*c/N

for i in range(0,N+1):
    if i < N/2:
        xi = dx1*i
    if i >= N/2:
        xi = 1 - c + dx2*(i - N/2)
    x.append(xi)


def f(x):
    return 1 - x

def usoln(x):
    return (exp(R) - exp(R*x))/(exp(R) - 1)


u0 = []

for j in range(0,N+1):
    u0.append(f(x[j]))

u = u0

for tn in t:
    u[0] = 1
    u[N] = 0
    for j in range(1,N):
        dxp = x[j+1] - x[j]
        dxm = x[j] - x[j-1]
        u[j] = u0[j] - dt*(u0[j] - u0[j-1])/dxm + (dt/R)*((u0[j+1] - u0[j])/dxp - (u0[j] - u0[j-1])/dxm)/dxp
    u0 = u

u_soln = []

for xj in x:
    u_soln.append(usoln(xj))


plt.plot(x,u_soln,label="Exact soln")
plt.plot(x,u,label=r"Numerical soln w/ N = ${}$".format(N))
plt.title(r"Solution for u(x,t) @ t=10 w/ $\Delta$t = ${}$".format(dt))
plt.xlabel("x")
plt.ylabel("u(x)")
plt.legend(loc="best")
plt.show()

E = []

for j in range(0,len(x)):
    err = abs(u[j] - u_soln[j])
    E.append(err)

print(max(E))