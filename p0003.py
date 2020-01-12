"""
Solution to Project Euler problem 3
Problem 1: https://projecteuler.net/problem=3
"""

def trial_division(number):
    """Trial division because modern computers are fast."""
    array = []               
    factor = 2
    while number > 1:         
        if number % factor == 0:   
            array.append(factor)  
            number /= factor
        else:            
            factor += 1       
    return array[-1]


if __name__ == "__main__":
    print(trial_division(600851475143))
    