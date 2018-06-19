#!/usr/bin/python
def main():

  val = input()
  count = 0
  while val > 0:
    val = val / 10
    count = count + 1
  print count

main()
