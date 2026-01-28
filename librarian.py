from data import books

def add_books():
    while True:
        id_of_book = int(input("Enter Book unique ID : "))
        name_of_book = input("Enter Name of Book : ")
        author_of_book = input("Author of book : ")
        quantity_of_book = int(input("Quality of book available : "))

        book = {
            "id": id_of_book,
            "book_name": name_of_book,
            "book_author": author_of_book,
            "book_quantity": quantity_of_book
        }

        books.append(book)

        option = input("Do you want to add more books : ")
        if option.lower() != "yes":
            break


def update_book() :
    book_id = int(input("Enter book ID to update: "))

    for book in books:
        if book["id"] == book_id:
            print("Book found:", book)

        ask = int(input('''Which thing you want to update : 
                    1. Book ID
                    2. Book Author
                    3. Book Name
                    4. Book Qunatity : '''))
        if ask == 1:
                book["id"] = int(input("Enter updated book id: "))
        elif ask == 2:
                book["book_author"] = input("Enter updated author name: ")
        elif ask == 3:
                book["book_name"] = input("Enter updated book name: ")
        elif ask == 4:
                book["book_quantity"] = int(input("Enter updated quantity: "))
        else:
                print("Invalid choice")

        print("Book updated successfully!")
        return

    print("Book not found.")


def view_book() :
        print("The records of books are : \n")
        for book in books:
            print(book)


def search_book():
    book_name = input("Enter book name to search: ")

    for book in books:
        if book["book_name"].lower() == book_name.lower():
            print("\nBook Found:")
            print(book)
            return

    print("Book not found.")

def librarian_menu ():
    print('''
1)Add Book
2)Update Book
3)View Books
4)Search Book
5)Logout        
          ''')
    choice = int(input("Please Enter your choice : "))
    if choice == 1:
        print("Add book selected")
        add_books()
        selection = input("Now what you want to do: ")
        if selection.lower() == "show menu" :
            librarian_menu()
            
    elif choice == 2:
        print("Update book selected")
        update_book()
        selection = input("Now what you want to do: ")
        if selection.lower() == "show menu" :
            librarian_menu()
    elif choice == 3:
        print("View book selected")
        view_book()
        selection = input("Now what you want to do: ")
        if selection.lower() == "show menu" :
            librarian_menu()
    elif choice == 4:
        print("Search book selected ")
        search_book()
        selection = input("Now what you want to do: ")
        if selection.lower() == "show menu" :
            librarian_menu()
    elif choice == 5:
        print("Logging out...")
        return

    else:
        print("Invalid Selection please try again...")