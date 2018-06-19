#!/usr/bin/python
def main():

  num = input()
  numnew = num
  digitlist = []
  soc = 0
  while numnew > 0:
      digit = numnew % 10
      numnew = numnew / 10
      digitlist.append(digit)
  power = int(len(digitlist))    
  for i in digitlist:
    soc = i ** power  + soc
  
  if num == soc:
    print "True"
  else:
    print "False"

main()
