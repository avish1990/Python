#!/usr/bin/python
def digit_sum(n):
  a = str(n)
  sum = 0
  for i in range(0,len(a)):
    b = n % 10
    sum += b
    n = n // 10
  print sum
   
digit_sum(8757585)
