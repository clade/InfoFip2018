# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 15:18:46 2018

@author: marti
"""

from TD_dioptres2 import *
import numpy as np

wave_length = 780e-6 #mm

n_LAH64 = 1.77694
n_SF11 = 1.76583
n_air = 1.0002992

plan = Dioptre(0, 1e5, n_air, n_SF11)
convexe = Dioptre(3, -100, n_SF11, n_air)

L378 = SystemeOptique([plan, convexe])

ecran = Dioptre(150, 1e5, n_air, n_air)

S0 = SystemeOptique(L378+[ecran])

r0 = Rayon([0,1,-10], [0,0,1])

liste_r0 = np.array([Rayon([0,h,-10], [0,0,1]) for h in np.linspace(-10, 10, 11)])

liste_faisceau = S0.calcul_faisceau(liste_r0)

S0.plot()
faisceau = S0.calcul_faisceau(r0)
#faisceau.plot()
for faisceau in liste_faisceau:
    faisceau.plot()
plt.grid()

kx, ky, kz = faisceau[-2].k
print(kx, ky, kz)
print(-1*kz/ky)

# __call__