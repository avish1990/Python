#!/usr/bin/python
def main():

  var = raw_input()
  try:
    newvar = int(var)
    print "This input is of type Integer."
  except:
    try:
      newvar = float(var)
      print "This input is of type Float."
    except:
      print "This input is of type string."


main()
