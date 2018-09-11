#!/usr/bin/python
pyth = []
i = 1
j = 2
while len(pyth) < 30:
  a = (j * j - i * i)  
  b = 2 * j * i
  c = ( j * j + i * i)
  pyth.append(sorted([a,b,c]))
  j += 1

for x in pyth:
  print x
