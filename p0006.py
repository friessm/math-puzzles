"""
Solution to Project Euler problem 6
https://projecteuler.net/problem=6
"""


def sum_of_squares(number):
    """
    Cubic function.

    1**2 + 2**2 + ... + n**2 can be expressed as a cubic function. 
    a*n**3 + b*n**2 + c*n + d where d = 0 because 0, for n = 0. 
    Solve 3 unknowns and voila 1/3*n*3 + 1/2*n**2 + 1/6*n.
    
    """
    return int(1/3*number**3 + 1/2*number**2 + 1/6*number)

def square_of_sums(number):
    """ 
    Square a triangular number.

    1,3,6,10,15,... is a triangular sequence and can therefor be solved
    with the simple formulae: n(n+1)/2 
    
    https://www.mathsisfun.com/algebra/triangular-numbers.html
    
    """
    return int((number*(number+1)/2)**2)

def sum_square_difference(number):
    return int(square_of_sums(number) - sum_of_squares(number))


if __name__ == '__main__':
    print(sum_square_difference(100))