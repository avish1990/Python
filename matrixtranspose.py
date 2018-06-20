#!/usr/bin/python
def main():
  
  listofp = []
  m = [int(x) for x in raw_input("Enter space sepertaed dimensions of list: ").split()]
  for i in range(0,m[0]):
    p = [int(x) for x in raw_input("Enter space seperated row %s for list: " % (i+1)).split()]  
    listofp.append(p)
  
  transp = [[listofp[j][i] for j in range(len(listofp))] for i in range(len(listofp[0]))]
  for i in transp:
    print ' '.join(map(str, i)) 
main()
