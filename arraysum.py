#!/usr/bin/python
def main():
  size = input()
  array = [ int(x) for x in raw_input().split() ]
  targetsum = input()
  for i in range(size):
    for j in range(size):
      arraysum = array[i] + array[j]
      if arraysum == targetsum:
        print True
        exit() 
  else:
    print False

main()
