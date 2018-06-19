#!/usr/bin/python
def main():

  total = input()
  array = []
  while total > 0:
      numbers = input()
      array.append(numbers)
      total = total - 1
  array = list(reversed(sorted(array)))
  print array[1]
      
main()
