from operations import (
    add_student,
    show_students,
    delete_student,
    update_student,
    search_student,
)
student_list=[]
while True:
    print("\n===== Student Management System=====")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Delete Student")
    print("4. Update Student")
    print("5. Search Student")
    print("10. Exit")



    choice=input("\nEnter Choice : ")

    if choice=='1':
        add_student(student_list)
    elif choice == '2':
        show_students(student_list)
    elif choice=='3':
        delete_student(student_list)
    elif choice=='4':
        update_student(student_list)
    elif choice=='5':
        search_student(student_list)
    elif choice=='10':
        print("The Programme Closed Successfully")
        break
    else:
        print("\nInvalid Choice")

