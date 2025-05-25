


class GrandFather:
    def greet(self):
        print("Hello from GrandFather")
        
class Father(GrandFather):
    def greet(self):
        print("Hello from Father")
        
class Child(Father):
    def greet(self):
        print("Hello from Child")
        
gf = GrandFather()
f = Father()
c = Child()

gf.greet()
f.greet()
c.greet()

# method overloading

class Shape:
    def area(self, a, b = 10):
        return a * b
    
shape1 = Shape()
print(shape1.area(5))   
print(shape1.area(5, 3))