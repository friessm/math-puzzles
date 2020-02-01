"""
Solution to Project Euler problem 4
https://projecteuler.net/problem=4
"""

def find_largest_palindrome(number):
    while number > 0:
        if str(number) == str(number)[::-1]:
            for i in range(999,0,-1):
                if number % i == 0 and number / i < 1000:
                    return number
        number -= 1
    return False


if __name__ == "__main__":
    """The largest palindrome that is the product of two 3-digit-numbers
    has to be smaller than 998001 (999x999).
    """

    print(find_largest_palindrome(998001))