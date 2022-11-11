"""
Title: Iterators task

First task: Given a number. Write iterator that prints n fibonacci numbers using __iter__ and __next__ methods.
Second task: Write iterator that prints n fibonacci numbers using __getitem__ method.

Example:
    Input: 11
    Output: 0 1 1 2 3 5 8 13 21 34 55
"""


class FirstFibonacciIterator:
    """
    Class to implement an iterator of Fibonacci numbers using __iter__ and __next__ methods.
    """
    def __init__(self, length: int):
        self.length = length
        self.n1 = 0
        self.n2 = 1

    def __iter__(self):
        self.step = 0
        return self

    def __next__(self):
        if self.step <= self.length:
            n0 = self.n1
            self.n1 = self.n2
            self.n2 = n0 + self.n1
            self.step += 1
            return n0
        else:
            raise StopIteration


class SecondFibonacciIterator:
    """
    Class to implement an iterator of Fibonacci numbers using __getitem__ method.
    """
    def __init__(self, length: int):
        self.length = length

    def __getitem__(self, item: int):
        if item < self.length:
            return self.__fib(item)
        raise IndexError

    def __fib(self, index: int):
        if index < 2:
            return index
        return self.__fib(index - 1) + self.__fib(index - 2)

    def __len__(self):
        return self.length


if __name__ == '__main__':
    first_iterator = list(FirstFibonacciIterator(11))
    print("First Fibonacci Iterator:", first_iterator)

    second_iterator = list(SecondFibonacciIterator(11))
    print("Second Fibonacci Iterator:", first_iterator)
