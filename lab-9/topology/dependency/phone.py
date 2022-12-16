class Phone:
    def __init__(self, battery_level: int = 0):
        self.battery_level = battery_level

    def charge_from(self, socket):
        while self.battery_level < 100 and socket.battery_level > 0:
            self.battery_level += 1
            socket.battery_level -= 1
