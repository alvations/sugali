# -*- coding: utf-8 -*-

import math, operator

def arithmetic_mean(x): # x is a list of values.
  """ Returns the arithmetic mean given a list of values. """
  return sum(x)/len(x)

def geometric_mean(x): # x is a list of values
  """ Returns the geometric mean given a list of values. """
  return math.pow(reduce(operator.mul, x, 1), 1/float(len(x)))

def arigeo_mean(x, threshold = 1e-10): # x is a list of values
  arith = arithmetic_mean(x)
  geo = geometric_mean(x)
  while math.fabs(arith - geo) > threshold: 
    [arith,geo] = [(arith + geo) / 2.0, math.sqrt(arith * geo)]
  return arith

'''
# Informal test
y= [1,3,5,7,8,3,5, 2342352, 45734523, 2342352362,246524]
print arithmetic_mean(y)
print geometric_mean(y)
print arigeo_mean(y)
'''