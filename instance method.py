


class Employee:
    company_name = "Ostad Company"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def display_info(self):
        print(f"Employee name: {self.name}\nEmployee salary: {self.salary}")
        
    @classmethod
    def change_company_name(cls, new_name):
        cls.company_name = new_name
        print(f"Company name changed to: {cls.company_name}")
        
obj1 = Employee("Rahim", 50000)
obj1.display_info()
obj1.change_company_name("ABC Company")
print(f"Company name: {obj1.company_name}")