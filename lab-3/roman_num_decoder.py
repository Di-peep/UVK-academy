"""
Title: Roman Numerals Decoder

Task: Given a string. Create a function that takes a Roman numeral as its argument and returns its value as a
    numeric decimal integer. You don't need to validate the form of the Roman numeral.
    Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately,
    starting with the leftmost digit and skipping any 0s. So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and
    2008 is rendered "MMVIII" (2000 = MM, 8 = VIII). The Roman numeral for 1666, "MDCLXVI", uses each letter in
    descending order.

Example:
    Input: XXI
    Output: 21
"""


def roman_to_int(line: str) -> int:
    roman = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }
    res = 0
    digit = line[-1]
    operation_flag = True

    for d in line[::-1]:
        if roman[d] < roman[digit]:
            operation_flag = False
        else:
            operation_flag = True
            digit = d

        if operation_flag:
            res += roman[d]
        else:
            res -= roman[d]

    return res


if __name__ == '__main__':
    print(f"Input: {'XXI'}\n"
          f"Output: {roman_to_int('XXI')}\n")

    print(f"Input: {'CLXIX'}\n"
          f"Output: {roman_to_int('CLXIX')}\n")
