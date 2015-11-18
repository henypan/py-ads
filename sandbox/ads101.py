__author__ = 'Henry Pan'


def gcd(m, n):
    while m % n != 0:
        oldm = m
        m = n
        n = oldm % n

    return n


print gcd(6, 4)



