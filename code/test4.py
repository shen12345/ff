#!/usr/bin/env python3

def f(x, n):
    return x ** n / f0(n)

def f0(n):
    result = 1
    for x in range(n+1):
        if x == 0:
            continue
        result *= x
    return result

def main(a_input):
    result = 0
    x = float(input("Please enter the x number: "))
    # num = int(input("Please enter the item number: "))
    for a in range(a_input):
        result += f(x,a)
    print("The first {} item sum is {}".format(a_input,result))
    return result

if __name__ == '__main__':
    for a in range(11):
        if a == 2 or a == 5 or a == 10:
            main(a)
