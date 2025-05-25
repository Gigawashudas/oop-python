


class School:
    school_name = "Ostad High School" # class variable
    
    def __init__(self, name):
        self.student_name = name #instance variable
    
sc1 = School("Rahim")
sc1.school_name = "XYZ School"

print(sc1.school_name)
print(sc1.student_name)

sc2 = School("Karim")

print(sc2.school_name)
print(sc2.student_name)