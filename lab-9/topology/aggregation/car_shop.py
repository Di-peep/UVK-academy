from topology.aggregation import Address


class CarShop:
    def __init__(self, title: str, address: Address):
        self.title = title
        self.address = address

    def take_shop_card(self):
        print(f"Our shop here: {self.address.city, self.address.street}")
