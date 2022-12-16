"""
Title: Class modifications pt.2

Task: Modify your existing topology classes with at least one abstract class.
    + Add magic methods to recieve description of the objects.
    + Override at least one comparison method.
    + Override at least one arithmetic method.
    + Override at least one copying method.
"""
from abc import ABC, abstractmethod
from copy import copy


class ChargerClient(ABC):
    @abstractmethod
    def charge_from(self, socket):
        pass


class Phone(ChargerClient):
    def __init__(self, battery_level: int = 0):
        self.battery_level = battery_level

    def charge_from(self, socket):
        while self.battery_level < 100 and socket.battery_level > 0:
            self.battery_level += 1
            socket.battery_level -= 1

    def __ge__(self, other):
        return self.battery_level >= other.battery_level

    def __doc__(self):
        return f"""I`m a phone (charger client) and my battery level: {self.battery_level}"""


class PowerBank:
    def __init__(self, battery_level: int = 200):
        self.battery_level = battery_level

    def __add__(self, other):
        return self.battery_level + other.battery_level

    def __copy__(self):
        my_copy = type(self)()
        my_copy.__dict__.update(self.__dict__)
        return my_copy

    def __doc__(self):
        return f"""I`m a power bank and my battery level: {self.battery_level}"""


class User:
    """My main task is charge phone or something else before outgoing."""
    @staticmethod
    def put_device_on_a_charger(device, charger):
        device.charge_from(charger)


if __name__ == '__main__':
    power_bank = PowerBank(120)
    phone = Phone()
    user = User()

    user.put_device_on_a_charger(phone, power_bank)

    print(f"Power bank: {power_bank.battery_level}")
    print(f"Phone: {phone.battery_level}")

    print(phone >= phone)
    print(power_bank + power_bank)

    copy_phone = copy(phone)
    print(id(phone), id(copy_phone))
