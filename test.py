#!/usr/bin/python
def digit_sum(n):
  n = str(n)
  sum = 0
  for i in range( 0 , len(n) ):
    a = n[i]
    a = int(a)   
    sum += a
    
  print sum
     

digit_sum(8757585)
