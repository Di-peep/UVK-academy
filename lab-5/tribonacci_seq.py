"""
Title: Tribonacci Sequence

Task: As the name may already reveal, it works basically like a Fibonacci, but summing the last 3 (instead of 2)
    numbers of the sequence to generate the next.
    Well, you may have guessed it by now, but to be clear: you need to create a fibonacci function
    that given a signature array/list, returns the first n elements - signature included of the so seeded sequence.
    Signature will always contain 3 numbers; n will always be a non-negative number; if n == 0, then return an empty
    array (except in C return NULL) and be ready for anything else which is not clearly specified ;)

Example:
    Input: [1, 1, 1], 8
    Output: [1, 1 ,1, 3, 5, 9, 17, 31]

    Input: [0, 0, 1], 9
    Output: [0, 0, 1, 1, 2, 4, 7, 13, 24]
"""
from functools import lru_cache


def check_input(trio: tuple, amount: int):
    """A function to check all possible input values."""
    if not isinstance(trio, tuple):
        print("Expected trio type is tuple")
        return False
    if len(trio) < 3:
        print("Length first trio must be 3!")
        return False
    if not all([isinstance(element, int) for element in trio + (amount,)]):
        print("Expected type is integer")
        return False
    if amount < 0:
        print("Amount must be non-negative")
        return False

    return True


@lru_cache(maxsize=32)
def get_tribonacci_number(trio: tuple, index: int):
    if index < 3:
        return trio[index]
    return \
        get_tribonacci_number(trio, index - 1) + \
        get_tribonacci_number(trio, index - 2) + \
        get_tribonacci_number(trio, index - 3)


def tribonacci_sequence(trio: tuple, amount: int):
    if check_input(trio, amount):
        return [get_tribonacci_number(trio, n) for n in range(amount)]

    return []


if __name__ == '__main__':
    print(tribonacci_sequence((1, 1, 1), 9))
