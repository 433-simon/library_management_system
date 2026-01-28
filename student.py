from data import books, students

def issue_book():
    student_id = int(input("Enter student roll no: "))

    for student in students:
        if student["student_id"] == student_id:
            break
    else:
        print("Student not found.")
        return

    book_name = input("Enter book name to issue: ")

    for book in books:
        if book["book_name"].lower() == book_name.lower():
            if book["book_quantity"] > 0:
                book["book_quantity"] -= 1
                print("Book issued successfully.")
            else:
                print("Book out of stock.")
            return

    print("Book not found.")


def add_student() :
    while True:
        student_roll_no = int(input("Enter student's roll no. : "))
        name_of_student = input("Enter student's name : ")
        number_of_student = int(input("Enter student's contact info : "))
        book_issued_by_student = input("Does student issued any book earlier : ")

        student = {
            "student_id" : student_roll_no,
            "student_name" : name_of_student,
            "student_number" : number_of_student,
            "student_issued_book" : book_issued_by_student
        }
        students.append(student)

        student_option = input("Do you want to add more students : ")
        if student_option.lower() != "yes" :
            break;


def return_book():
    book_name = input("Enter name of book you want to return: ")

    for book in books:
        if book["book_name"].lower() == book_name.lower():
            book["book_quantity"] += 1
            print("Book returned successfully.")
            return

    print("Invalid book name.")


def student_menu ():
    while True: 
        print('''
1) Issue Book
2) Return Book
3) Logout
          ''')
        choice = int(input("Please Enter your choice : "))
        if choice == 1:
            issue_book()
        elif choice == 2:
            return_book()
        elif choice == 3:
            print("Looging out...")
            return
        else:
            print("Invalid Selection please try again...")