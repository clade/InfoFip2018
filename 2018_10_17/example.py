#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 16:28:27 2018

@author: pierre
"""

#from calcul_formel import Symbol

#print(Symbol('x'))

#import os
#print(os.getcwd())
#
#import sys
#sys.path.append(r'C:\blablab\balblbal')

import math

from symcalc.symbol import x, y, t
from symcalc import Symbol, sin

e = x + sin(y*t)

assert repr(e)=="x + sin(y * t)"

default_value = {'x':1, 'y':2, 't':3}

assert e.evaluate(**default_value)== 1 + math.sin(2*3)

try:
    e.evaluate()
except Exception:
    pass
else:
    raise Exception('Il y aurait du avoir une erreur')

e = (x + y)*t
repr(eval(repr(e)))==repr(e)
    