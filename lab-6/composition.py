"""
Title: Class topology: Composition

Task: Choose any existing topology of objects that surround us and represent it via classes.
    Implement class hierarchy that will use different relations between objects.
    Use classmethods and staticmethods.
    Create UML diagram to represent the topology and relations inside of it.

Note: Create at least 3 classes
"""
from random import randint


class Passport:
    def __init__(self, first_name: str, last_name: str):
        self.passport_id = randint(10_000, 100_000)
        self.first_name = first_name
        self.last_name = last_name


class BankAccount:
    def __init__(self, bank_account=0):
        self.bank_id = randint(10_000, 100_000)
        self.bank_account = bank_account

    def transfer_to_bank_account(self, transfer: int):
        self.bank_account += transfer


class Person:
    def __init__(self, first_name, last_name, money=0):
        self.passport = Passport(first_name, last_name)
        self.bank_account = BankAccount(money)

    def who_i_am(self):
        print(f"I`m {self.passport.first_name} {self.passport.last_name}")

    def how_much_i_have(self):
        print(f"Bank account: {self.bank_account.bank_account}")


if __name__ == '__main__':
    person = Person('Name', 'Last', 1000)
    person.who_i_am()
    person.bank_account.transfer_to_bank_account(2000)
    person.how_much_i_have()
