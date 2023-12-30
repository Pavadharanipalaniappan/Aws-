class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model)
        self.year = year

    def display_info(self):
        super().display_info()
        print(f"Year: {self.year}")
        print("Type: Car")

class Bike(Vehicle):
    def __init__(self, brand, model, engine_size):
        super().__init__(brand, model)
        self.engine_size = engine_size

    def display_info(self):
        super().display_info()
        print(f"Engine Size: {self.engine_size}")
        print("Type: Bike")

class BMW(Car):
    def __init__(self, model, year, series):
        super().__init__("BMW", model, year)
        self.series = series

    def display_info(self):
        super().display_info()
        print(f"Series: {self.series}")

class Royal(Bike):
    def __init__(self, model, engine_size, style):
        super().__init__("Royal Enfield", model, engine_size)
        self.style = style

    def display_info(self):
        super().display_info()
        print(f"Style: {self.style}")


car = Car("Toyota", "Camry", 2022)
bike = Bike("Honda", "CBR1000RR", "1000cc")
bmw = BMW("X5", 2023, "X Series")
royal = Royal("Classic 350", "350cc", "Cruiser")


car.display_info()
print("\n")
bike.display_info()
print("\n")
bmw.display_info()
print("\n")
royal.display_info()
