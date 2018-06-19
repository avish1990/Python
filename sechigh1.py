#!/usr/bin/python
def main():

  total = input()
  array = list(reversed(sorted([int(x) for x in raw_input().split()]))) 
  print array[1]
      
main()
