#!/usr/bin/python
def is_prime(x):
  for n in range( 4 , x-1 ):
    if x % n == 0:
      print"%s is not prime" % n
    else:
      print "%s is prime" % n



is_prime(10)
