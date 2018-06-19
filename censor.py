#!/usr/bin/python
def censor(text,word):
    textsplit = text.split()
    for i in textsplit:
      if i == word:
        n = len(word)
        word = "*" * len(word)
        text = text.replace(i,word)
    print text

censor("Fuck you want","you")
