class Shape:
    def area(self):
        print("Calculating area of the shape")
        
class Polygon(Shape):
    def sides(self):
        print("Polygon has multiple sides")
        
class Rectangle(Polygon):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
    
rec = Rectangle(5, 3)
rec.sides()
print(rec.area())