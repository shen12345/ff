#!/usr/bin/env python3

x, y = 1, 1
num = 0
for a in range(30):
    num += 1
    if a != 29:
        print("%7d"%x, end = ' ')
    else:
        print("%7d"%x)
    x, y = y, x + y
    
