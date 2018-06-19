#!/usr/bin/python

def remove_duplicates(lst):
  orglst = []
  for i in lst:
    if i not in orglst:
      orglst.append(i)
  print orglst

lst = [1,2,3,4,5,4,2]
remove_duplicates(lst)
