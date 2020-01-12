"""
Solution to Project Euler problem 3
Problem 1: https://projecteuler.net/problem=3
"""

def trial_division(number):
    """Trial division because modern computers are fast."""
    
    last_factor = 0            
    factor = 2
    while number > 1:         
        if number % factor == 0:   
            last_factor = factor
            number /= factor
        else:            
            factor += 1
    return last_factor


if __name__ == "__main__":
    print(trial_division(600851475143))
    