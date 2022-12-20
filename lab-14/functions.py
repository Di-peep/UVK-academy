def is_symmetrical(line: str):
    return line[:len(line) // 2] == line[len(line) // 2:]


def is_palindrome(line: str):
    return line == line[::-1]


def multiply(a, b):
    return a.__mul__(b)


def is_balanced(line: str):
    while line:
        for brackets in ('()', '[]', '{}'):
            if brackets in line:
                line = line.replace(brackets, '')
                break
        else:
            return False
    return True
