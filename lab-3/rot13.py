"""
Title: ROT13

Task: Given the word, the task is to obfuscate it.
    According to Wikipedia, ROT13 (http://en.wikipedia.org/wiki/ROT13) is frequently used to obfuscate phrases on USENET.

Hint: For this task you're only supposed to substitute characters. Not spaces, punctuation, numbers etc.

Example:
    Input: EBG13 rknzcyr.
    Output: ROT13 example.

    Input: This is my first ROT13 excercise!
    Output: Guvf vf zl svefg EBG13 rkprepvfr!
"""


def save_case(line: str) -> list:
    """A function to save the case of letters."""
    return list(map(lambda char: ord('A') <= ord(char) <= ord('Z'), line))


def rot13(line: str) -> str:
    res = ''
    case_line = save_case(line)

    for i, char in enumerate(line.lower()):
        if ord('a') + 13 <= ord(char) + 13 <= ord('z'):
            rchar = chr(ord(char) + 13)
        elif ord('z') < ord(char) + 13 <= ord('z') + 13:
            rchar = chr(ord(char) + 13 - ord('z') + ord('a') - 1)
        else:
            rchar = char

        if case_line[i]:
            res += rchar.upper()
        else:
            res += rchar

    return res


if __name__ == '__main__':
    print(f"Input: {'EBG13 rknzcyr.'}\n"
          f"Output: {rot13('EBG13 rknzcyr.')}\n")

    print(f"Input: {'This is my first ROT13 excercise!'}\n"
          f"Output: {rot13('This is my first ROT13 excercise!')}\n")
