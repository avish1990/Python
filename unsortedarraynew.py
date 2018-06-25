#!/usr/bin/python
def main():
  length = input()
  array = [ int(x) for x in raw_input().split() ]
  for i in range(len(array)):
    if array[i] != sorted(array)[i]:
      firstindice = i
      break
  j = len(array) - 1
  while j > 0:
    if array[j] != sorted(array)[j]:
      lastindice = j + 1
      break
    j = j - 1
  output = array[firstindice:lastindice] 
  output = str(output).strip('[]')
  print ",".join(output).replace(",", "")
main()
