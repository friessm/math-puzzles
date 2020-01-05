"""
Solution to Project Euler problem 1
Problem 1: https://projecteuler.net/problem=1
"""
def multiple_of_three_or_five(upper_bound):
    multiples_list = []
    for number in range(1, upper_bound):
        if number % 3 == 0 or number % 5 == 0:
            multiples_list.append(number)
    return sum(multiples_list)


if __name__ == "__main__":
    print(multiple_of_three_or_five(1000))
    