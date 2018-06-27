#!/usr/bin/python
def main():

  size = input()
  array = [int(x) for x in raw_input().split()]
  array = list(sorted(array))
  i = 0
  while i < size - 1:
    if array[i+1] != array[i] + 1:
      print False 
      exit()
    i = i + 1
  print True

main()
