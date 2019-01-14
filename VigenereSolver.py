# -*- coding: utf-8 -*-

import sys

args = sys.argv

if (3 != len(args)):
    print('')
    print('Usage: python %s <ENCRYPTED> <KEY>' % (args[0]))
    print('')
    exit(-1)
else:
    #c = 'llkjmlmpadkkc'
    #key = 'thisisalilkey'
    c = args[1].strip()
    key = args[2].strip()


# Make Vigenere-square.
list2d = []
line = []
for n in range(0x41, 0x5b):
    line.append(chr(n))

for n in range(0x41, 0x5b):
    list2d.append(list(line))
    top = line[0]
    del line[0]
    line.append(top)

# 
c_upper = c.upper()
key_upper = key.upper()

index = 0
plain_text = []
for a in c_upper:
    #print("%s, %s" % (a, key_upper[index]))
    # 横
    x = list2d[0].index(key_upper[index])
    # 縦
    y = list2d[x].index(a)
    plain_text.append(list2d[0][y])
    index += 1

print('%s\n' % ''.join(plain_text))

