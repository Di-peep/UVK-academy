"""
Title: IP validation task

Task: Write an algorithm that will identify valid IPv4 addresses in dot-decimal format.
    IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.

Note: Create the main class for that task and the descriptor for getting and setting ip values.
"""


class IPDescriptor:
    def __init__(self):
        self.ip = '0.0.0.0'

    def __set__(self, instance, value):
        if self.check_ip_code(value):
            self.ip = value
            print('Value updated.')
        else:
            print('Incorrect value')

    def __get__(self, instance, owner):
        return self.ip

    @staticmethod
    def check_ip_code(ip_code: str) -> bool:
        test_funcs = {
            'check_len': lambda ip: len(ip.split('.')) == 4,
            'check_type': lambda ip: all(d.isdigit() for d in ip.split('.')),
            'check_range': lambda ip: all(0 <= int(d) <= 255 for d in ip.split('.'))
        }
        return all(test(ip_code) for test in test_funcs.values())


class IP:
    value = IPDescriptor()

    
if __name__ == '__main__':
    ip = IP()
    ip.value = '123.123.123.0'
    print(ip.value)
