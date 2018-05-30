#!/usr/bin/env python3

F = 0

while F <= 200:
    C = (F-32)/1.8
    print("When F is {:3d}, the C is {:6.2f}".format(F,C))
    F += 10
