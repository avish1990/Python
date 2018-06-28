#!/usr/bin/python
def main():
  
  dimensions = [int(x) for x in raw_input().split()]
  array = [[int(x) for x in raw_input().split()] for i in range(0,dimensions[0])]
  rowsum = [sum(i) for i in array]
  for i in range(len(rowsum)):
    if sum(rowsum) / dimensions[0] == rowsum[0]:
      print "Equal"
      break
    elif max(rowsum) == rowsum[i]:
      print "Row %d" % (i+1)
    

main()
