#!/usr/bin/python
def main():
  
  items = input()
  dictionary = sorted([raw_input() for i in range(items)])
  print [word for word in dictionary]  

main()
