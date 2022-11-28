__all__ = ['PowerBank', 'Phone', 'User']


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
