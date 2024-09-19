"""
Équation de diffusion/chaleur (1D) :

∂u     ∂²u
-- = D --- = 0,  x = [0, L], t > 0
∂t     ∂x²

u(t = 0) = 20°C
u(x = 0) = 100°C
u(x = L) = 100°C

Résolution à l'aide des différences finies pour l'espace et Euler explicite pour le temps :

u^(n+1)_i - u^n_i     u^n_(i-1) - 2u^n_i + u^n_(i+1)
----------------- = D ------------------------------ = 0
        Δt                          Δx²

"""

import numpy as np
import matplotlib.pyplot as plt
plt.style.use("dark_background")

L = 1.
D = 1.
Ti = 20.
Te = 100.

nx = 64
x = np.linspace(0, L, nx+1)
dx = x[1] - x[0]

tf = 0.1
dt = dx**2/(2*D)
alpha = D*dt/(dx**2)
t = np.arange(0, tf, dt)
nt = len(t)

u = np.zeros((nt, nx+1))
u[0] = Ti
u[:, 0] = Te
u[:, -1] = Te

for n in range(1, nt):
        u[n, 1:-1] = u[n-1, 1:-1] + alpha * (u[n-1, :-2] - 2*u[n-1, 1:-1] + u[n-1, 2:])

for n in range(nt):
        if (n%100 == 0):
                plotlabel = "t = %1.2f" % (n * dt)
                plt.plot(x, u[n, :], label=plotlabel, color=plt.get_cmap('winter')(float(n) / nt))

    
#plt.xlabel("x")
#plt.ylabel(r"$u(x,\,t)$")

#plt.legend(loc="best")
plt.show()
