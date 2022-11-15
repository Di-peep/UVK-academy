"""
Title: Class topology: Aggregation

Task: Choose any existing topology of objects that surround us and represent it via classes.
    Implement class hierarchy that will use different relations between objects.
    Use classmethods and staticmethods.
    Create UML diagram to represent the topology and relations inside of it.

Note: Create at least 3 classes
"""


class Address:
    def __init__(self, city: str, street: str):
        self.city = city
        self.street = street


class CarShop:
    def __init__(self, title: str, address: Address):
        self.title = title
        self.address = address

    def take_shop_card(self):
        print(f"Our shop here: {self.address.city, self.address.street}")


class Car:
    def __init__(self, model: str, store: CarShop):
        self.model = model
        self.store = store

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

    car_1.about_me()
    car_3.about_me()
