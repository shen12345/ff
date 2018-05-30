#!/usr/bin/env python3

for F in range(201):
    if F % 10 == 0:
        C = ( F - 32 ) / 1.8
        print("When the F is {:3d}, the C is {:6.2f}".format(F, C))
