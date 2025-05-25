


class GrandFather:
    def __init__(self, color, first_name):
        self.color = color
        self.first_name = first_name
        
    def gf(self):
        print("im from grandfather")
        
class Father(GrandFather):
    def __init__(self, color, first_name, hobby):
        super().__init__(color, first_name)
        self.hobby = hobby
        
    def father(self):
        print("im from father")
        
                
class Children(Father, GrandFather):
    def __init__(self, color, first_name, hobby, fashion):
        super().__init__(color, first_name, hobby)
        self.fashion = fashion

gf1 = GrandFather("white", "Rahim")
f1 = Father("black", "Karim", "cricket")
# print(f1.first_name)

c1 = Children("red", "Salim", "football", "modern")
c1.gf()
c1.father()
print(c1.fashion, c1.hobby, c1.first_name, c1.color)

