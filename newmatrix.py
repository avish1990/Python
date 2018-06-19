#!/usr/bin/python
# Performs addition of two matrices.
def main():
  
  listofp = []
  listofq = []
  m = [int(x) for x in raw_input("Enter dimenions of list1: ").split()]
  for i in range(0,m[0]):
    p = [int(x) for x in raw_input("Enter row for list1: ").split()]  
    for j in p:
      listofp.append(j)
 
  n = [int(x) for x in raw_input("Enter dimenions of list2: ").split()]   
  for i in range(0,n[0]):
    q = [int(x) for x in raw_input("Enter row for list2: ").split()]   
    for j in q:
      listofq.append(j)
 
  sumofpq = [listofp[i]+listofq[i] for i in range(0,len(listofp))]  
  matrix = [[sumofpq[j*m[1] + i] for i in range(m[1])] for j in range(m[0])]
  for i in matrix:
    print ' '.join(map(str, i)) 
main()
