"""
Title: Perfect numbers generator

Task: Given the number, the task to return n perfect numbers.
    In number theory, a perfect number is a positive integer that is equal to the sum of its positive divisors,
    excluding the number itself. For instance, 6 has divisors 1, 2 and 3 (excluding itself), and 1 + 2 + 3 = 6,
    so 6 is a perfect number.

Example:
    Input: 3
    Output: 6, 28, 496
"""


def generator_prime_numbers(n: int):
    i = 0
    digit = 1
    prime_numbers = {2, 3, 5}

    while i < n:
        digit += 1
        for divisor in prime_numbers:
            if digit % divisor == 0 and digit != divisor:
                break
        else:
            prime_numbers.add(digit)
            yield digit
            i += 1


def get_perfect_number(n: int) -> [int]:
    ans = []
    generator = generator_prime_numbers(n)
    for p in generator:
        ans.append(2 ** (p - 1) * (2 ** p - 1))

    return ans


if __name__ == '__main__':
    print(get_perfect_number(4))
