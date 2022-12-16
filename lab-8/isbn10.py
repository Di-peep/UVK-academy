"""
Title: ISBN-10 or IP modifications

Task: Update the decorator used for task from lab4 (choose ISBN-10 or IP) to be the class with
    overrided method `__call__()`.
"""


class ISBN10:
    def __call__(self, isbn10: str = None, *args, **kwargs):
        if not isbn10:
            print('Pls, give an isbn10 code..')
        elif self.check_isbn10(isbn10):
            print('Your isbn10 code is correct')
        else:
            print('Your isbn10 code is incorrect')

    @staticmethod
    def check_isbn10(isbn_code: str) -> bool:
        isbn_list_copy = list(isbn_code)
        if isbn_list_copy[-1] == 'X':
            isbn_list_copy[-1] = 10

        test_funcs = {
            'check_len': lambda isbn10: len(isbn10) == 10,
            'check_type': lambda isbn10: all(d.isdigit() for d in isbn10),
            'check_sum': lambda isbn10: sum([(i + 1) * int(digit) for i, digit in enumerate(isbn10)]) % 11 == 0
        }

        return all(test(isbn_list_copy) for test in test_funcs.values())


if __name__ == '__main__':
    isbn = ISBN10()
    isbn('1112223339')
    isbn('A112223A31')
