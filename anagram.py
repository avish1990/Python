#!/usr/bin/python

def anagram(word1,word2):
  list1 = sorted([ i for i in word1])
  list2 = sorted([ i for i in word2])
  if list1 == list2:
    print "anagram"
  else:
    print "not anagram"



#anagram("avinash","avinash")
anagram(raw_input(), raw_input())
