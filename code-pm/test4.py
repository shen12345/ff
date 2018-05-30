#!/usr/bin/env python3

def f0(n):
    result = 1
    for a in range(n+1):
        if a == 0:
            continue
        result *= a
    return result

def f(x,n):
    return x ** n / f0(n)

def main():
    x = float(input("Please enter the x value: "))
    ex = 0
    for a in range(11):
        if a == 2 or a == 5 or a == 10:
            for p in range(a):
                ex += f(x,p)
            print(ex)

if __name__ == '__main__':
    main()
