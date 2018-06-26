#!/usr/bin/python
def main():

  binary = list(reversed([ int(i) for i in raw_input() ]))
  decimal = [ 2 ** i for i in range(len(binary)) if binary[i] == 1 ] 
  print sum(decimal)
    
main()
