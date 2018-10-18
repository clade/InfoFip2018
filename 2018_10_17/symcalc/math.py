import math

from .base import Function

class MathFunction(Function):
    def display(self, *args):
        return '{}({})'.format(self.function_name,self.args[0].display())


class Sin(MathFunction):     
    function_name = 'sin'
    math_function = math.sin


sin = Sin