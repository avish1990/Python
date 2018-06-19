#!/usr/bin/python
a = input()
b = input()
def main():
  count = 0
  total = 1
  notprime = []
  
  if a == 1:
    for i in range(a+3,b):
      total = total + 1
      for num in range(2,i-1):
        if i % num == 0:
          notprime.append(i)
    final = total - len(sorted(set(notprime)))
    print final + 2
  elif a == 2:
      for i in range(a+2,b):
        total = total + 1
        for num in range(2,i-1):
          if i % num == 0:
            notprime.append(i)
      final = total - len(sorted(set(notprime)))
      print final + 2
  elif a == 3:
      for i in range(a+1,b):
        total = total + 1
        for num in range(2,i-1):
          if i % num == 0:
            notprime.append(i)
      final = total - len(sorted(set(notprime)))
      print final + 1
  elif a >= 3 and a <= 10000:
      for i in range(a,b):
        total = total + 2
        for num in range(2,i-1):
          if i % num == 0:
            notprime.append(i)
      print total - len(sorted(set(notprime)))
main()

