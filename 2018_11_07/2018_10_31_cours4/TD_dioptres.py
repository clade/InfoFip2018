# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 15:20:52 2018

@author: marti
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve

class Dioptre(object):
    diametre = 25.4
    def __init__(self, z0, R, n1, n2, diametre=None):
        self.z0 = z0
        self.R = float(R)
        if diametre is not None:
            self.diametre = diametre
        self.n1 = n1
        self.n2 = n2
        self.z_center = z0+R
    
    def __repr__(self):
        return 'Dioptre(z0={}, R={}, n1={}, n2={}, diametre={})'.format(self.z0, self.R, self.n1, self.n2, self.diametre)
    
    def plot(self):
        theta_max = np.arcsin(self.diametre/2/self.R)
        theta = np.linspace(-theta_max, theta_max)
        x = self.z_center - self.R*np.cos(theta)
        y = self.R*np.sin(theta)
        plt.subplot(2,1,1)
        plt.plot(x, y)
        plt.subplot(2,1,2)
        plt.plot(x, y)
        
    def traversee(self, rayon):
        p1 = rayon.p0
        k1 = rayon.k
        def fct(t):
            x, y, z = p1 + t*k1 - np.array([0,0,self.z_center])
            return x**2+y**2+z**2 - self.R**2
        ti = (-p1[2]+self.z_center+self.R)/k1[2]     
        tsol = fsolve(fct, ti)[0]
        p2 = p1 + tsol*k1
        if p2[0]**2+p2[1]**2 > self.diametre**2 or tsol < 0:
            return Rayon(p2, k1)
        
        n = (p2 - np.array([0,0,self.z_center]))/np.sqrt(((p2 - np.array([0,0,self.z_center]))**2).sum())
        kn = (k1*n).sum()
        k_parallele = k1 - n * kn
        norme_k_parallele = np.sqrt((k_parallele**2).sum())
        if self.n2**2 - norme_k_parallele**2 < 0:
            return Rayon(p2, np.array([0,0,0]))
        alpha = np.sqrt(self.n2**2 - norme_k_parallele**2)
        if alpha*kn <= 0:
            alpha = -alpha
        k2 = k_parallele + alpha*n
        return Rayon(p2, k2)
            
        
class Rayon(object):
    def __init__(self, p0, k, n=None):
        self.p0 = np.array(p0)
        self.k = np.array(k)
        if n is not None:
            self.normalize(n)
            
    def __repr__(self):
        return 'Rayon(p0={}, k={})'.format(self.p0, self.k)
    
    def normalize(self, n):
        kx, ky, kz = self.k
        norme_k = np.sqrt(kx**2+ky**2+kz**2)
        self.k = np.array([kx/norme_k*n, ky/norme_k*n, kz/norme_k*n])
# ce n'est pas très judicieux

class Faisceau(list):
    def plot(self):
        if len(self) < 2:
            print('Le faisceau doit contenir au moins 2 rayons')
        z, x, y = [], [], []
        for rayon in self:
            z.append(rayon.p0[2])
            x.append(rayon.p0[0])
            y.append(rayon.p0[1])
        plt.subplot(2,1,1)
        plt.plot(z, x)
        plt.subplot(2,1,2)
        plt.plot(z, y)
        
class SystemeOptique(list):
    def calcul_faisceau(self, r0):
        faisceau = Faisceau()
        faisceau.append(r0)
        for dioptre in self:
            print(faisceau[-1].p0)
            faisceau.append(dioptre.traversee(faisceau[-1]))
        return faisceau
    
    def plot(self):
        for dioptre in self:
            dioptre.plot()
            
#wave_length = 780e-6 #mm
#
#n_LAH64 = 1.77694
#n_SF11 = 1.76583
#n_air = 1.0002992
#
#S1 = Dioptre(0, -4.7, n_air, n_SF11, diametre=3)
#S2 = Dioptre(1.5, 1e10, n_SF11, n_air, diametre=3)
#
#LC2969 = SystemeOptique()
#LC2969.append(S1)
#LC2969.append(S2)
#
#plan_image = Dioptre(100, 1e10, 30, n_air, n_air)
#
#system = SystemeOptique()
#system.extend(LC2969)
#system.append(plan_image)
#
#r0 = Rayon(p0=np.array([0,1,-5]), k=np.array([0,0, 1]), n=n_air)
#faisceau = system.calcul_faisceau(r0)
#
#plt.figure()
#LC2969.plot()
##faisceau.plot()
#plt.show()
#    
#rayon = Rayon(np.array([0,0,-3]), np.array([0,0,1]))
#dioptre = Dioptre(0, 6, 1, 1.5)   