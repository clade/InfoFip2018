# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 14:25:08 2018

@author: marti
"""

from TD_dioptres2 import *

wave_length = 780e-6 #mm

n_LAH64 = 1.77694
n_SF11 = 1.76583
n_air = 1.0002992

S1 = Dioptre(0, -4.7, n_air, n_SF11, diametre=3)
S2 = Dioptre(1.5, 1e4, n_SF11, n_air, diametre=3)

S1.plot()
S2.plot()

r0 = Rayon(p0=np.array([0,1,-5]), k=np.array([0,0, 1]), n=n_air)
r1 = Rayon(p0=np.array([0,0,-5]), k=np.array([0,0, 1]), n=n_air)

print(S1.intersection(r0))
print(S2.intersection(r0))

print(S1.traversee(r0))
print(S2.traversee(r0))

print(S1.traversee(r1))
print(S2.traversee(r1))

LC2969 = SystemeOptique()
LC2969.append(S1)
LC2969.append(S2)

plan_image = Dioptre(100, 1e10, 30, n_air, n_air)

system = SystemeOptique()
system.extend(LC2969)
system.append(plan_image)

r0 = Rayon(p0=np.array([0,1,-5]), k=np.array([0,0, 1]), n=n_air)
faisceau = system.calcul_faisceau(r0)

plt.figure()
LC2969.plot()
faisceau.plot()
plt.show()
    
rayon = Rayon(np.array([0,0,-3]), np.array([0,0,1]))
dioptre = Dioptre(0, 6, 1, 1.5)   