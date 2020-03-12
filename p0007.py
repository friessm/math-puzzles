"""
Solution to Project Euler problem 7
https://projecteuler.net/problem=7
"""

from math import sqrt, log, ceil

def sieve_of_eratosthenes(number):
    """
    Sieve of Eratosthenes

    Return a list of all prime numbers from 2 to roughly the 
    number-th (10001) prime. Standard implementation with
    some minor tweaks.

    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

    """

    upper_bound = ceil(number*log(number*log(number)))
    integer_list = [x for x in range(2, upper_bound+1)]

    for i in range(0, int(sqrt(upper_bound))):
        # n is prime if it is not changed to 0. Then, update all multiples 
        # of n. Offset by -2 because integer_list[0] = 2.
        n = integer_list[i]
        if n != 0:
            for j in range(n*n-2, upper_bound-1, n):
                integer_list[j] = 0    
    return integer_list

def nth_prime(integer_list, number):
    """
    Return the number-th prime

    Parameters
    :param list integer_list: list consisting of prime numbers.
    :param integer number: the n-th prime

    """
    prime_count = 0
    for x in range(0, len(integer_list)):
        if integer_list[x] != 0:
            prime_count += 1
            if prime_count == number:
                return integer_list[x]
    
def find_nth_prime(number):
    return nth_prime(sieve_of_eratosthenes(number), number)     


if __name__ == '__main__':
    print(find_nth_prime(10001))