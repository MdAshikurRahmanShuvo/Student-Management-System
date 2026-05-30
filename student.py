class Student:
    def __init__(self,name,roll,cgpa):
        self.name=name
        self.roll=roll
        self.cgpa=cgpa
    def show_student_details(self):
        print("Student Details ")
        print("Name : ",self.name)
        print("Roll : ", self.roll)
        print("CGPA : ", self.cgpa)