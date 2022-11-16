"""
Title: Class modifications: Aggregation

Task: Modify your existing topology classes with dataclass or any other library for simplification.
"""
from dataclasses import dataclass


@dataclass
class Address:
    city: str
    street: str


@dataclass
class CarShop:
    title: str
    address: Address

    def take_shop_card(self):
        print(f"Our shop here: {self.address.city, self.address.street}")


@dataclass
class Car:
    model: str
    store: CarShop

    def about_me(self):
        print(f"Model: {self.model}")
        print(f"Store: {self.store.title}")


if __name__ == '__main__':
    random_address = Address('Seattle', 'University st.')

    first_car_shop = CarShop('CarShop', random_address)
    car_1 = Car('BMW X1', first_car_shop)
    car_2 = Car('BMW X2', first_car_shop)

    second_car_shop = CarShop('Wheels', random_address)
    car_3 = Car('BMW X3', second_car_shop)
    car_4 = Car('BMW X4', second_car_shop)

    print(car_1)
    print(car_3)
