


class Car:
    def __init__(self):
        self.brand = ""
        self.model = ""
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def __init__(self, brand = "TOYOTA", model = "COROLLA"):
        self.brand = brand
        self.model = model
        

car1 = Car()
print(car1.brand, car1.model)

car2 = Car("HONDA", "CIVIC")
print(car2.brand, car2.model)