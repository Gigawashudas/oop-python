


class GrandFather:
    def __init__(self, color, first_name):
        self.color = color
        self.first_name = first_name
        
class Father(GrandFather):
    def __init__(self, color, first_name, hobby):
        super().__init__(color, first_name)
        self.hobby = hobby

gf1 = GrandFather("white", "Rahim")
f1 = Father("black", "Karim", "cricket")
print(f1.first_name)