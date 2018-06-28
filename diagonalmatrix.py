#!/usr/bin/python
def main():
  
  dimensions = [int(x) for x in raw_input().split()]
  array = [[int(x) for x in raw_input().split()] for i in range(0,dimensions[0])]
  diag1 = [ array[i][i] for i in range(dimensions[0])]
  diag2 = [ list(reversed(array))[i][i] for i in range(dimensions[0])]
  if sum(diag1) > sum(diag2):
    print "Diagonal1"
  elif sum(diag1) < sum(diag2):
    print "Diagonal2"
  else:
    print "Equal"

main()
