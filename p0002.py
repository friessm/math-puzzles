"""
Solution to Project Euler problem 2
https://projecteuler.net/problem=2
"""

def even_fibunacci(number_1, number_2):
    fib = 0 
    res = 0
    
    # Starting with n=1 and n-1=0. Fn+1 = Fn + Fn-1.
    while fib <= 4000000:
        fib = number_1 + number_2       
        if fib % 2 == 0: res += fib
        number_1, number_2 = fib, number_1
    return res

if __name__ == "__main__":
    print(even_fibunacci(0, 1))