"""
Title: ISBN-10 Validation

Task: ISBN-10 identifiers are ten digits long.
    The first nine characters are digits 0-9. The last digit can be 0-9 or X, to indicate a value of 10.
    An ISBN-10 number is valid if the sum of the digits multiplied by their position modulo 11 equals zero.

Note: Create the decorator that validates if the passed to inner function isbn value is correct.
    In case of incorrect isbn format, user should see the error message.

Examples of correct isbn-10 addresses: 1112223339, 1234554321, 048665088X
Examples of incorrect isbn-10 addresses: 111222333, 1112223339X, 1234512345, X123456788
"""

from functools import wraps


def isbn_validator(func):
    @wraps(func)
    def wrapper(isbn: str):
        isbn_copy = list(isbn)
        if isbn_copy[-1] == 'X':
            isbn_copy[-1] = 10

        if len(isbn_copy) != 10:
            print('Incorrect length isbn-10')
        elif not all(d.isdigit() for d in isbn_copy):
            print('Incorrect type isbn-10')
        elif sum([(i + 1) * int(digit) for i, digit in enumerate(isbn_copy)]) % 11 == 0:
            func(isbn)
        else:
            print('Incorrect isbn-10')

    return wrapper


@isbn_validator
def print_isbn(isbn: str):
    print(isbn)


if __name__ == '__main__':
    print_isbn('1112223339')
    print_isbn('A112223A31')
