"""
Title: Class topology: Association

Task: Choose any existing topology of objects that surround us and represent it via classes.
    Implement class hierarchy that will use different relations between objects.
    Use classmethods and staticmethods.
    Create UML diagram to represent the topology and relations inside of it.

Note: Create at least 3 classes
"""


class PowerBank:
    def __init__(self, battery_level: int = 200):
        self.battery_level = battery_level


class Phone:
    def __init__(self, battery_level: int = 0):
        self.battery_level = battery_level

    def charge_from(self, socket):
        while self.battery_level < 100 and socket.battery_level > 0:
            self.battery_level += 1
            socket.battery_level -= 1


class User:
    def __init__(self, my_phone: Phone, my_power_bank: PowerBank):
        self.my_phone = my_phone
        self.my_power_bank = my_power_bank

    def put_my_phone_on_the_charger(self):
        self.my_phone.charge_from(self.my_power_bank)


if __name__ == '__main__':
    power_bank = PowerBank()
    phone = Phone()
    user = User(phone, power_bank)

    user.put_my_phone_on_the_charger()

    print(f"Power bank: {user.my_power_bank.battery_level}")
    print(f"Phone: {user.my_phone.battery_level}")
