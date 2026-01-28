# main.py
from student import student_menu
from librarian import librarian_menu

print("Welcome to Library Management System!")
role = input("Enter role (student/librarian): ")

if role.lower() == "student":
    student_menu()
elif role.lower() == "librarian":
    librarian_menu()
else:
    print("Invalid role")
