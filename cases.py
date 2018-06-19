#!/usr/bin/python
import re
def main():

  string = raw_input()
  string = re.escape(string)
  print string
  up = 0
  lo = 0
  sp = 0
  for i in string:
    
    if i == " " or i == "'" or i == "?" or i == "!" or i == "," or i == "." or i == ":" or i == ";":
      sp = sp + 1
    elif i.lower() == i:
      lo = lo + 1  
    elif i.upper() == i:
      up = up + 1
  print up
  print lo
main()
