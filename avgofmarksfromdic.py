# Sampe Input
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika

# Sample Output --> 56.00

#!/usr/bin/python
n = int(raw_input())
dic = [[ x for x in raw_input().split()] for i in range(n)]
req = raw_input()

for i in dic:
  if i[0] == req:
    print '%.2f' % ((float(i[1]) + float(i[2]) + float(i[3])) / 3)
