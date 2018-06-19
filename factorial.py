#!/usr/bin/python
def factorial(x):
  total = 1
  while x > 1:
    total  = total * x
    x = x - 1
  print total

factorial(5)
