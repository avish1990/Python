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
  for i in digitlist:
    soc = i * i * i + soc
  print soc
  print num    
  if num == soc:
    print "yes"
  else:
    print "no"

main()
