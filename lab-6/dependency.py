"""
Title: Class topology: Dependency

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
