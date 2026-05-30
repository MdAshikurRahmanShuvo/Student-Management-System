from student import Student
def add_student(student_list):
    print("\n=====  Add Student =====")
    name=input("Enter Name : ")
    roll=input("Enter Roll : ")
    exists=False
    for student in student_list:
        if student.roll==roll:
            exists=True
    if exists==True:
        print("\nRoll Already Exists")
        return
    cgpa=float(input("Enter CGPA : "))
    if cgpa<0 or cgpa>4:
        print("\nInvalid CGPA")
        return
    student=Student(name,roll,cgpa)
    student_list.append(student)
    print("Student Added Successfully")

def show_students(student_list):
    print("\n=====  All Students  =====")
    if len(student_list)==0:
        print("No Students Found")
    else:
        for student in student_list:
            student.show_student_details()


def delete_student(student_list):
    print("\n===== Delete Student =====")
    roll=input("Enter Roll : ")
    found=False
    for student in student_list:
        if student.roll==roll:
            student_list.remove(student)
            print("Student Deleted Successfully")
            found=True
            break
    if found == False:
        print("\nStudent Not Found")


def update_student(student_list):
    print("\n=====  Update Student =====")
    roll=input("Enter Roll :")
    found=False
    for student in student_list:
        if student.roll==roll:
            new_name=input("Enter Updated Name : ")
            new_cgpa = float(input("Enter Updated CGPA : "))
            student.name=new_name
            student.cgpa=new_cgpa
            print("\nStudent Updated Successfully")
            found=True
            break
    if found==False:
        print("\nStudent Not Found")


def search_student(student_list):
    print("\n=====  Search Student =====")
    roll = input("Enter Roll :")
    found = False
    for student in student_list:
        if student.roll==roll:
            student.show_student_details()
            found=True
            break
    if found==False:
        print("\nStudent Not Found")

