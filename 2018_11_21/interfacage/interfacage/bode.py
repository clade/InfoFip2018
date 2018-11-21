import inspect
from numpy import sin, pi, arange
import numpy as np
import matplotlib.pyplot as plt


from scipy.optimize import curve_fit


def my_curve_fit(fit_function, xdata, ydata, p0={}):
    args, _, _, defaults = inspect.getargspec(fit_function)
    defaults = list(defaults)
    for cle, val in p0.items():
        i = args.index(cle)
        defaults[i-1] = val
    popt, _ = curve_fit(fit_function, xdata, ydata, p0=defaults)
    out = dict(zip(args[1:], popt))
    return out


class FitSinus(object):
    _popt = None
    
    def __init__(self, temps, datay, frequence):
        self.temps = temps
        self.datay = datay
        self.frequence_ini = frequence
    
    @staticmethod
    def fit_sinus(x, amplitude=1, offset=0, phase=0, frequence=10):
        return offset + amplitude*sin(2*pi*frequence*x + phase)
    
    def fit(self):
        amplitude = (self.datay.max()-self.datay.min())/2
        offset = (self.datay.max()+self.datay.min())/2
        p0 = {'amplitude': amplitude, 'offset':offset, 'frequence':self.frequence_ini}
        popt = my_curve_fit(self.fit_sinus, self.temps, self.datay, p0=p0)
        if popt['amplitude']<0:
            popt['amplitude'] = -popt['amplitude']
            popt['phase'] += pi
        return popt
    
    @property
    def popt(self):
        if self._popt is None:
            self._popt = self.fit()
        return self._popt
    
    @property
    def phase(self):
        return self.popt['phase']
    
    @property
    def amplitude(self):
        return self.popt['amplitude']

    def plot(self):
        plt.plot(self.temps,self.datay,'o')
        t = np.linspace(self.temps.min(),self.temps.max(),100)
        plt.plot(t,self.fit_sinus(t, **self.popt))
        plt.xlabel("Temps")
        plt.ylabel("Amplitude")


class BodePoint(object):
    def __init__(self, temps, signal_reference, signal_filtre, frequence):
        self.temps = temps
        self.signal_reference = signal_reference
        self.signal_filtre = signal_filtre
        self.frequence = frequence
        self._sinus_filtre = FitSinus(temps, signal_filtre, frequence)
        self._sinus_ref = FitSinus(temps, signal_reference, frequence)
    
    def plot(self):
        plt.subplot(2, 1, 1)
        self._sinus_ref.plot()
        plt.subplot(2, 1, 2)
        self._sinus_filtre.plot()
        
        
    @property
    def gain(self):
        return self._sinus_filtre.amplitude/self._sinus_ref.amplitude
    
    @property
    def dephasage(self):
        return (self._sinus_filtre.phase - self._sinus_ref.phase)%(2*pi)


class BodeDiagramme(object):
    def __init__(self):
        self.liste_points = []
        
    def ajoute_bode_point(self, bode_point):
        self.liste_points.append(bode_point)
        
    def plot(self):
        plt.subplot(2, 1, 1)
        plt.loglog(self.frequence, self.gain)
        plt.subplot(2, 1, 2)
        plt.semilogx(self.frequence, self.dephasage)
        
    @property
    def frequence(self):
        return np.array([point.frequence for point in self.liste_points])
    
    @property
    def gain(self):
        return np.array([point.gain for point in self.liste_points])
    
    @property
    def dephasage(self):
        return np.array([point.dephasage for point in self.liste_points])
