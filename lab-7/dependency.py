"""
Title: Class modifications: Dependency

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


class User:
    @staticmethod
    def put_device_on_a_charger(device, charger):
        device.charge_from(charger)


if __name__ == '__main__':
    power_bank = PowerBank(120)
    phone = Phone()
    print(power_bank)
    print(phone)

    user = User()
    user.put_device_on_a_charger(phone, power_bank)

    print(f"Power bank: {power_bank.battery_level}")
    print(f"Phone: {phone.battery_level}")
