"""
Title: To square(root) or not to square(root)

Task: Given an array of number. Write a method, that will get a number array as parameter and will process
    every number from this array. Return a new array with processing every number of the input-array like this:
    If the number has an rational square root, take this, otherwise square the number.

Example:
    Input:  [4,3,9,7,2,1]
    Output: [2,9,3,49,4,1]

    Input: [1.21,0,9]
    Output: [1.1,0,3]
"""


def check_root(number):
    number *= 1.0
    if len(str(number ** 0.5)) <= len(str(number)):
        return True
    return False


def process_arr(arr: list) -> list:
    return [(n ** 2, n ** 0.5)[check_root(n)] for n in arr]


if __name__ == '__main__':
    print(f"Input: [1.21, 0, 9]\n"
          f"Output: {process_arr([1.21, 0, 9])})\n")

    print(f"Input: [1.2, 1_000_000, 1]\n"
          f"Output: {process_arr([1.2, 1_000_000, 1])})\n")
