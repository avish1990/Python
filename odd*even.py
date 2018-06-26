#!/usr/bin/python
def main():
  size = input()
  array = [int(x) for x in raw_input().split()]
  odd = 0
  even = 0
  for num in array:
    if num % 2 != 0:
      odd += num
    elif num % 2 == 0:
      even += num
  print odd * even
main()
