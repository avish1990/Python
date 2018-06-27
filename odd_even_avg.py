#!/usr/bin/python
def main():

  size = input()
  array = [int(x) for x in raw_input().split()]
  odd = 0
  even = 0
  countodd = 0
  counteven = 0
  avgodd = 0
  avgeven = 0
  for num in array:
    if num % 2 != 0:
      odd += num
      countodd = countodd + 1
    elif num % 2 == 0:
      even += num
      counteven = counteven + 1
  if counteven != 0 and countodd != 0:
    avgodd = int(round(odd / float(countodd)))
    avgeven = int(round(even / float(counteven)))
  elif counteven == 0:
    avgodd = int(round(odd / float(countodd)))
  elif countodd == 0:
    avgeven = int(round(even / float(counteven)))
  print avgodd
  print avgeven  
  print avgodd + avgeven
   

main()
