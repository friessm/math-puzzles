"""
Solution to Project Euler problem 10
https://projecteuler.net/problem=10
"""


def sieve_of_eratosthenes(number):
    """
    Sieve of Eratosthenes

    Return the sum of all prime numbers from 2 to number. 
    Standard implementation of Sieve with some optimisations.
    
    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

    """

    # Create list from 0 to number
    sieve_list = [True for x in range(0, number+1)]

    # Remove multiples of 2
    for i in range(4, number+1, 2):
        sieve_list[i] = False

    # Iterate over the odd numbers
    for i in range(3, number+1, 2):
        if sieve_list[i] == True:
            # i is prime and odd. Use i+i to only iterate over odd 
            # multiples of i.
            for j in range(i*i, number+1, i+i):
                sieve_list[j] = False
    
    return sum([i for i in range(2, number+1) if sieve_list[i] == True])



if __name__ == '__main__':
    print(sieve_of_eratosthenes(2000000))