#!/usr/bin/env python3

num = 0
n = int(input("Please enter a integer number: "))

x = 0

while n > num:
    num += 1
    int_input = float(input("Please enter a float number: "))
    x += int_input

x = x / num

print("The everage of", num , "number is ", x)
