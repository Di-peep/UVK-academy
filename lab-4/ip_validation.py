"""
Title: IP Validation

Task: Write an algorithm that will identify valid IPv4 addresses in dot-decimal format.
    IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.

Note: Create the decorator that validates if the passed to inner function ip value is correct.
    In case of incorrect ip format, user should see the error message.

Examples of correct ip addresses: 1.2.3.4, 123.45.67.89
Examples of incorrect ip addresses: 1.2.3, 1.2.3.4.5, 123.456.78.90, 123.045.067.089
"""
from functools import wraps


def ip_validator(func):
    @wraps(func)
    def wrapper(ip: str):
        if len(ip.split('.')) != 4:
            print('IP must consist of four octets!')
        elif not all(d.isdigit() for d in ip.split('.')):
            print('IP must consist only numbers!')
        elif not all(0 <= int(d) <= 255 for d in ip.split('.')):
            print('IP values must be between 0 and 255!')
        else:
            func(ip)

    return wrapper


@ip_validator
def print_ip(ip: str):
    print(ip)


if __name__ == '__main__':
    print_ip('123.456.78.90')
    print_ip('123')
