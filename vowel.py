#!/usr/bin/python
def anti_vowel(text):
  t = ""
  vowels = {"a","e","i","o","u","A","E","I","O","U"}
  for i in text:
    for x in vowels:
      if i == x:
	i = ""
      #text = text.strip(x)
      #text = text.replace(x,"")
      else:   
	i = i 
    t = t + i
  print t
anti_vowel("avinash")
