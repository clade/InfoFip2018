# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 14:36:47 2018

@author: marti
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve

def scalaire(a, b):
    return np.sum(a*b)

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
        self.c = np.array([0,0,self.z_center])
    
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
        
    def intersection(self, rayon):
        p0 = rayon.p0
        k = rayon.k
        c = self.c
        
        a = scalaire(k,k)
        b = 2*scalaire(p0-c, k)
        c = scalaire(p0-c, p0-c) - self.R**2
        
        if self.R >= 0:
            sign = -1
        else:
            sign = 1
        
        t = 1/(2*a)*(-b + sign*np.sqrt(b**2-4*a*c))

        return p0+k*t
        
    def traversee(self, rayon):
        p2 = self.intersection(rayon)
        k = rayon.k
        c = self.c
        
        n = (p2 - c)/np.sqrt(scalaire(p2-c, p2-c))
        
        k_parallele = k - n * scalaire(k, n)
        
        norme_k_parallele = np.sqrt(scalaire(k_parallele, k_parallele))
        
        if self.n2**2 - norme_k_parallele**2 < 0:
            raise Exception('Réflexion totale non traitée ici.')
        
        alpha = np.sqrt(self.n2**2 - norme_k_parallele**2)
        if alpha*scalaire(k, n) <= 0:
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

class Faisceau(list):
    def plot(self):
        if len(self) < 2:
            raise Exception('Le faisceau doit contenir au moins 2 rayons')
        plt.subplot(2,1,1)
        plt.plot(self.z, self.x, 'o-')
        plt.subplot(2,1,2)
        plt.plot(self.z, self.y, 'o-')
        
    @property
    def x(self):
        return [elm.p0[0] for elm in self]
    
    @property
    def y(self):
        return [elm.p0[1] for elm in self]
    
    @property
    def z(self):
        return [elm.p0[2] for elm in self]
        
class SystemeOptique(list):
    def _calcul_faisceau(self, r0):
        faisceau = Faisceau()
        faisceau.append(r0)
        for dioptre in self:
            faisceau.append(dioptre.traversee(faisceau[-1]))
        return faisceau
   
    def calcul_faisceau(self, r0):
        if isinstance(r0, Rayon):
            return self._calcul_faisceau(r0)
        else : #il faudrait mettre if is iterable ?
            return [self._calcul_faisceau(elm) for elm in r0]
    
    def plot(self):
        for dioptre in self:
            dioptre.plot()