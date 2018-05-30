#!/user/bin/env python3

x, y = 1, 1
num = 0

while num < 30:
    num += 1
    print("the {:2d} item of Fibonicci is {:7d}".format(num, x))
    x, y = y, x + y
