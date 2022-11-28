from topology.aggregation import CarShop


class Car:
    def __init__(self, model: str, store: CarShop):
        self.model = model
        self.store = store

    def about_me(self):
        print(f"Model: {self.model}")
        print(f"Store: {self.store.title}")
