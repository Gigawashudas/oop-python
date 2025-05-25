


# Association
class Laptop:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Student:
    def __init__(self, name, laptop):
        self.name = name
        self.laptop = laptop
        
    def show_laptop_info(self):
        print(f"Student Name: {self.name}")
        print(f"Laptop Brand: {self.laptop.brand}")
        print(f"Laptop Model: {self.laptop.model}")

lp1 = Laptop("Dell", "XPS 13")
student = Student("Alice", lp1)
student.show_laptop_info()

# Aggregation
class Department:
    def __init__(self, name):
        self.name = name
        
class University:
    def __init__(self, name):
        self.name = name
        self.departments = []
        
    def add_department(self, department):
        self.departments.append(department)
        
    def show_departments(self):
        print(f"University: {self.name}")
        for dept in self.departments:
            print(f"Department: {dept.name}")
            
dept1 = Department("Computer Science")
dept2 = Department("Mathematics")
university = University("XYZ University")
university.add_department(dept1)
university.add_department(dept2)
university.show_departments()

# Composition
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    def show_horsepower(self):
        print(f"Engine Horsepower: {self.horsepower}")
        
class Car:
    def __init__(self, brand, model, horsepower):
        self.brand = brand
        self.model = model
        self.engine = Engine(horsepower)
        
    def show_info(self):
        print(f"Car Brand: {self.brand}")
        print(f"Car Model: {self.model}")
        self.engine.show_horsepower()
        
car = Car("Toyota", "Corolla", 130)
car.show_info()