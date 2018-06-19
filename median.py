#!/usr/bin/python
def median(lstold):
  lst = sorted(lstold)
  if len(lst) % 2 == 0:
    j = len(lst) / 2
    value1 = lst[j]
    value2 = lst[j-1]
    median = ( value1 + value2 ) / 2.0
    
    return median
  elif len(lst) % 2 == 1:
    value = len(lst) // 2
   # value = value - 0.5
    value = int(value)
    
    print lst[value]
    

lstold = [2,3,9,88,2,4,1]
median(lstold)
