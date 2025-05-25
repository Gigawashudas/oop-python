


class Car:
    def driver(self):
        return "driving a car"
    
class Bike:
    def driver(self):
        return "driving a bike"
    
class VehicleFactory:
    @staticmethod
    def get_vehicle(vehicle_type):
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "bike":
            return Bike()
        else:
            raise ValueError("Unknown vehicle type")
        
vehicle = VehicleFactory.get_vehicle("car")
print(vehicle.driver())