"""Calculating Greatest Common Divisor using Euclid's Algorithm
"""


def Euclid_GCD(a, b):
    if b >= a:
        a, b = b, a

    while b != 0:
        c = b
        b = a % b
        a = c

    return a

print(Euclid_GCD(1071,462))

print(Euclid_GCD(462,1071))
