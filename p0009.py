"""
Solution to Project Euler problem 9
https://projecteuler.net/problem=9
"""

from math import prod, sqrt

def generate_primitive_triple(s):
    """ Euclid's formula.

    Using Euclid's formula to find primitive triplets. Return the sum
    of a, b and c if a + b + c = s, for some s.

    """
    
    for m in range(2, int(sqrt(s / 2))):   
        # Increment n and keep m > n > 0.
        for n in range(1, m) : 
            # Switch a and b from Euclid's formula to ensure a > b
            b = m * m - n * n 
            a = 2 * m * n 
            c = m * m + n * n 

            if sum([a, b, c]) == s:
                return prod([a, b, c])

if __name__ == '__main__':
    print(generate_primitive_triple(1000))