#!/usr/bin/python
def main():
  size = input()
  array = [int(x) for x in raw_input().split()]
  nomin = []
  nomax = []
  for i in array:
    for j in array:
      if i > j:
        nomin.append(i)
        break
  #    elif i < j:
  #      nomax.append(j)
  #      break
  
  print nomin
  print sum(array) - sum(nomin)
  #print nomax
main()
