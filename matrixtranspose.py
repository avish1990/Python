#!/usr/bin/python
def main():
  
  dimensions = [int(x) for x in raw_input("Enter space separated dimensions of list: ").split()]
  array = [[int(x) for x in raw_input("Enter space separated row %s for list: " % (i+1)).split()] for i in range(0,dimensions[0])]
  trans_array = [[array[j][i] for j in range(len(array))] for i in range(len(array[0]))]
  for i in trans_array:
    print ' '.join(map(str, i)) 
main()
