


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary
        
    def get_salary(self, password):
        if password == "1234":
            print(self._salary)
        else:
            print("Access Denied")
    
    def set_salary(self, new_salary, password):
        if password == "1234":
            self._salary = new_salary
            print("Salary updated successfully")
        else:
            print("Access Denied")
    
obj1 = Employee("Rahim", 50000)

obj1._salary = 70000
obj1.get_salary("1234")
obj1.get_salary("0000")

obj1.set_salary(80000, "1234")
obj1.get_salary("1234")