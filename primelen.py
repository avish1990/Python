#!/usr/bin/python
a = input()
b = input()
def main():
  count = 0
  total = 1
  notprime = []
  if a != 1:
    for i in range(a,b):
      total = total + 1
      for num in range(2,i-1):
        if i % num == 0:
          notprime.append(i)
    print total - len(sorted(set(notprime)))
main()
