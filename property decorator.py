


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary
        
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, new_salary):
        if new_salary < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = new_salary
        print("Salary updated successfully")
    
obj1 = Employee("Rahim", 50000)
print(obj1.salary)
obj1.salary = 70000
print(obj1.salary)