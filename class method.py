


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
        
    def display_info(self):
        print(f"Car brand: {self.brand}\nCar model: {self.model}")
        

car1 = Car()
car1.display_info()

car2 = Car("HONDA", "CIVIC")
car2.display_info()

