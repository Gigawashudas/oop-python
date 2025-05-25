


class School:
    # Class variable
    school_name = "ABC High School"
    
    @staticmethod
    def calculate_grade(marks):
        if marks >= 90:
            return "A"
        elif marks >= 80:
            return "B"
        elif marks >= 70:
            return "C"
        elif marks >= 60:
            return "D"
        else:
            return "F"

print(School.calculate_grade(85))
    