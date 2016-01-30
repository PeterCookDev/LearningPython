"""Calculating Square Roots using Newton's Algorithm
"""

import math

def Newton_Sqrt(a):
    epsilon = 0.0000001
    if a > 2:
        x = a - 1
    else:
        x = a


    while True:
        y = (x + a / x) / 2
        if (x - y) < epsilon:
            break
        x = y

    return y


for x in range(1,9):
    print('%-3i%-12f%-12f%-18f' % (x, Newton_Sqrt(x), math.sqrt(x), Newton_Sqrt(x)-math.sqrt(x)))
