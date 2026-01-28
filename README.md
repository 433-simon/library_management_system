# 📚 Library Management System (Core Python)

A **CLI-based Library Management System** built using **pure Core Python**, without any external libraries or frameworks. This project focuses on strengthening Python fundamentals such as lists, dictionaries, functions, loops, conditional logic, and modular programming.

---

## 🚀 Project Overview

This system simulates a real-world library environment with **role-based access**:

* **Librarian**: Manages books (add, update, view, search)
* **Student**: Issues and returns books

The project was initially developed as a single script and later **refactored into a modular, multi-file structure** to improve readability, scalability, and maintainability — following real software engineering practices.

---

## 🧠 Key Concepts Covered

* Lists & list methods
* Dictionaries & dictionary methods
* String handling & string methods
* Functions & modular programming
* Conditional statements
* Loops
* Input validation (basic)
* Separation of concerns

---

## 📁 Project Structure

```
library_project/
│
├── main.py          # Entry point (login & role handling)
├── data.py          # Shared in-memory data (books, students)
├── librarian.py     # Librarian-related functionalities
├── student.py       # Student-related functionalities
└── README.md        # Project documentation
```

---

## ⚙️ Features

### 👨‍💼 Librarian

* Add new books
* Update existing book details
* View all books
* Search books by name

### 👩‍🎓 Student

* Issue a book
* Return a book

---

## ▶️ How to Run the Project

1. Clone or download the repository
2. Navigate to the project folder
3. Run the following command:

```bash
python main.py
```

4. Select your role (`student` or `librarian`) when prompted

---

## 🛠️ Technologies Used

* **Language**: Python
* **Type**: Command Line Interface (CLI)
* **Storage**: In-memory (lists & dictionaries)

---

## 📌 Future Enhancements

* Prevent duplicate book IDs
* Track issued books per student
* Add file-based storage using JSON
* Improve input validation

---

## 🙌 Author

**Simon**
Python Developer | CS Student

---

⭐ If you found this project useful, feel free to star the repository!
