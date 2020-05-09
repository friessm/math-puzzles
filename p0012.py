"""
Solution to Project Euler problem 12
https://projecteuler.net/problem=12
"""


from collections import Counter
from math import prod


def triangular_number(n):
    """ 
    https://www.mathsisfun.com/algebra/triangular-numbers.html 
    https://en.wikipedia.org/wiki/Triangular_number 
    
    """
    return int(n*(n+1) / 2)


def trial_division(n):
    """ Trial division.

    Find all prime numbers and their exponents of n.
    
    Output:
    pe_list = [(p1, e1), (p2, e2), (...)]
    p = prime number
    e = exponent of p

    """

    pe = []
    e = 0
    while n % 2 == 0:
        pe.append(2)
        e += 1
        n /= 2

    # Only test odd numbers up to sqrt(n)
    f = 3
    e = 0
    while f * f <= n:
        if n % f == 0:
            pe.append(f)
            n /= f
        else:
            e = 0
            f += 2
    
    if n != 1: pe.append(int(n))
    return Counter(pe).most_common(None)


def number_of_divisors(pe_list):
    """ Find all divisors based on the prime number exponents.
    
    d(n) = (e1 + 1) * (e2 + 1) * (...) * (en + 1)
    Best explanation: http://mathforum.org/library/drmath/view/55843.html
    
    """
    return prod([int(y + 1) for x, y in pe_list])


def find_number_divisors(d):
    i = 1
    while True:
        tn = triangular_number(i)     
        if (number_of_divisors(trial_division(tn))) > d:
            return tn
        i += 1


if __name__ == '__main__':
    print(find_number_divisors(500))