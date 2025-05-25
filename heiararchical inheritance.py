class Vehicle:
    def engine_type(self):
        print("Vehicle engine type: Internal Combustion Engine")
    
class Car(Vehicle):
    def num_doors(self):
        print("Car has four doors")

class Truck(Vehicle):
    def load_capacity(self):
        print("Truck can carry 10 tons")
        
car = Car()
car.engine_type()
car.num_doors()
truck = Truck()
truck.engine_type()
truck.load_capacity()