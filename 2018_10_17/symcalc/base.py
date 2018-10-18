#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numbers
import operator

class Expr(object):
    def binary_operator(self, other, operator):
        if isinstance(other, numbers.Number):
            other = Number(other)
        if isinstance(other, Expr):
            return operator(self, other)
        return NotImplemented

    def reversed_binary_operator(self, other, operator):
        if isinstance(other, numbers.Number):
            other = Number(other)
        if isinstance(other, Expr):
            return operator(other, self)
        return NotImplemented

    def __add__(self, other):
        return self.binary_operator(other, Sum)
        
    def __mul__(self, other):
        return self.binary_operator(other, Prod)

    def __truediv__(self, other):
        return self.binary_operator(other, Div)

    def __sub__(self, other):
        return self.binary_operator(other, Sub)

    def __radd__(self, other):
        return self.reversed_binary_operator(other, Sum)
 
    def __rmul__(self, other):
        return self.reversed_binary_operator(other, Prod)

    def __rtruediv__(self, other):
        return self.reversed_binary_operator(other, Div)

    def __rsub__(self, other):
        return self.reversed_binary_operator(other, Sub)

    def __neg__(self):
        return Neg(self)
    
    def __repr__(self):
        return self.display()

class Node(Expr):
    pass

class Leave(Expr):
    pass

class Symbol(Leave):
    def __init__(self, symbole):
        self.symb = symbole
        
    def display(self, *args):
        return self.symb
    
    def evaluate(self, **kwd):
        try:
            return kwd[self.symb]
        except KeyError:
            raise Exception("La valeur de {} n'est pas définie".format(self.symb))
class Number(Leave):
    def __init__(self, nombre):
        self.nbre = nombre
        
    def display(self, *args):
        return str(self.nbre)
    
    def evaluate(self, **kwd):
        return self.nbre

class Function(Node):
    """ Function with an arbitrary number of arguments """
    def __init__(self, *args):
        self.args = args

    def evaluate(self, **kwd):
        evaluated_args = [elm.evaluate(**kwd) for elm in self.args]
        return self.math_function(*evaluated_args)

class BinaryOperator(Function):
        
    def display(self, parent_priority=0):
        if parent_priority>self.priority:
            fmt_str = '({} {} {})'
        else:
            fmt_str = '{} {} {}'
        return fmt_str.format(self.args[0].display(self.priority), 
                self.operator_name, self.args[1].display(self.priority))

class Sum(BinaryOperator):
    priority = 0
    operator_name = '+'
    math_function=operator.add
    

class Prod(BinaryOperator):
    priority = 1
    operator_name = '*'
    math_function=operator.mul

class Div(BinaryOperator):
    priority = 2
    operator_name = '/'
    math_function=operator.truediv


class Sub(BinaryOperator):
    priority = 0.5
    operator_name = '-'
    math_function=operator.sub


class UnitaryOperator(Function):
    
    def display(self, parent_priority=0):
        if parent_priority>self.priority:
            fmt_str = '({}{})'
        else:
            fmt_str = '{}{}'
        return fmt_str.format(self.unitary_symbol, 
                              self.args[0].display(self.priority))
            
class Neg(UnitaryOperator):
    priority = 0.5
    unitary_symbol = "-"
    math_function = operator.neg
        
