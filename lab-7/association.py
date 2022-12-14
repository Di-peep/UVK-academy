"""
Title: Class modifications: Association

Task: Modify your existing topology classes with dataclass or any other library for simplification.
"""
from dataclasses import dataclass


@dataclass
class PowerBank:
    battery_level: int = 200


@dataclass
class Phone:
    battery_level: int = 0

    def charge_from(self, socket):
        while self.battery_level < 100 and socket.battery_level > 0:
            self.battery_level += 1
            socket.battery_level -= 1


@dataclass
class User:
    my_phone: Phone
    my_power_bank: PowerBank

    def put_my_phone_on_the_charger(self):
        self.my_phone.charge_from(self.my_power_bank)


if __name__ == '__main__':
    power_bank = PowerBank()
    phone = Phone()
    user = User(phone, power_bank)
    print(user)

    user.put_my_phone_on_the_charger()

    print(f"Power bank: {user.my_power_bank.battery_level}")
    print(f"Phone: {user.my_phone.battery_level}")
