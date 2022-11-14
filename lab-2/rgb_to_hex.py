"""
Title: RGB To Hex Conversion

Task: Given 3 numbers. Write the function so that passing in RGB decimal values will result in a hexadecimal
    representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range
    must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

Example:
    Input: 255, 255, 255
    Output: FFFFFF

    Input: 255, 255, 300
    Output: FFFFFF
"""


def to_hex(x: int) -> str:
    if x < 0:
        x = 0
    if x > 255:
        x = 255
    return hex(x)[2:].upper()


def check_len(hex_code: str):
    if len(hex_code) < 2:
        return '0' + hex_code
    return hex_code


def rgb_to_hex(r: int, g: int, b: int) -> str:
    rgb = map(to_hex, [r, g, b])
    rgb = map(check_len, rgb)
    return ''.join(rgb)


if __name__ == '__main__':
    print(f"RGB: 300, 300, 300:\n"
          f"HEX: {rgb_to_hex(300, 300, 300)}\n")

    print(f"RGB: 300, 0, 1:\n"
          f"HEX: {rgb_to_hex(300, 0, 1)}\n")
