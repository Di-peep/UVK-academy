"""
Title: Class modifications: Composition

Task: Modify your existing topology classes with dataclass or any other library for simplification.
"""
from dataclasses import dataclass
from random import randint


@dataclass
class Passport:
    first_name: str
    last_name: str
    passport_id: int = randint(10_000, 100_000)


@dataclass
class BankAccount:
    bank_account: int = 0
    bank_id: int = randint(10_000, 100_000)

    def transfer_to_bank_account(self, transfer: int):
        self.bank_account += transfer


@dataclass
class Person:
    first_name: str
    last_name: str
    money: int = 0

    def __post_init__(self):
        self.passport = Passport(self.first_name, self.last_name)
        self.bank_account = BankAccount(self.money)

    def who_i_am(self):
        print(f"I`m {self.passport.first_name} {self.passport.last_name}")

    def how_much_i_have(self):
        print(f"Bank account: {self.bank_account.bank_account}")


if __name__ == '__main__':
    person = Person('Name', 'Last', 1000)
    print(person)

    person.who_i_am()
    person.bank_account.transfer_to_bank_account(2000)
    person.how_much_i_have()
