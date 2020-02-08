"""
Solution to Project Euler problem 5
https://projecteuler.net/problem=5
"""

from numpy import prod

def lowest_common_multiple(upper_bound):
    """ 
    Find the lowest common multiple (LCM).
    
    LCM(a, b), where b > a. Increment by b, because b mod a can 
    never be 0 since b > a. Check if a mod multiple(b) is 0. If 
    yes, then the LCM has been found. If no, increment by b. 

    """
    
    number_list = [x for x in range(upper_bound, 0, -1)]
    worst_case = prod(number_list)

    for number in range(upper_bound, worst_case + 1, upper_bound):
        for integer in number_list:
            if number % integer != 0:
                break
            if number % integer == 0 and integer == 1:
                return number
    return False

if __name__ == "__main__":
    print(lowest_common_multiple(20))