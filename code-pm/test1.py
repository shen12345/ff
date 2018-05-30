#!/usr/bin/env python3

num = 0
n = int(input("Please enter a interger number: "))
x = 0
while num < n:
    num += 1
    x_input = float(input("Please input the number: "))
    x += x_input

x = x / n

print('=' * 36 )
print("The average of {:2d} numbers is {:5.2f}".format(n,x))
