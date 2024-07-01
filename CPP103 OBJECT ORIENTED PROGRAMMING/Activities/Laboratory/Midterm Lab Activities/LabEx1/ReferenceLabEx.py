#Encapsulation
class Book:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id

#Inheritance
class EnglishBook(Book):
    def __init__(self, title, author, book_id, location):
        super().__init__(title, author, book_id)
        self.location = location

    def get_book_info(self):
        print(f"Title: {self.title} , Author: {self.author}, ID: {self.book_id}, Location: {self.location}")

class Library:
    def __init__(self):
        self.books = []

#abstraction
#setters
    def add_book(self, title, author, book_id, location):
        self.books.append(EnglishBook(title, author, book_id, location))

#getters
    def get_library_books(self):
        for book in self.books:
            print(book.get_book_info())

    def save_books_to_file(self, filename):
        file = open(filename, "a")
        
        for book in self.books:
            file.write(f"{book.title},{book.author},{book.book_id},{book.location}\n")
                
    def load_books_from_file(self, filename):
        file = open(filename, "r")

        for book in file:
            title, author, book_id, location = book.strip().split(",") 
            self.books.append(EnglishBook(title, author, book_id, location))   

    def transaction_menu(self):
        print("1. Add a Book")
        print("2. View All Books")
        print("3. Save books to file")
        print("4. Load books from file")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            book_id = input("Enter Book ID: ")
            location = input("Enter location/shelf: ")

            self.add_book(title, author, book_id, location)

        elif choice == "2":
            self.get_library_books()

        elif choice == "3":
            filename = input("Enter the filename: ")
            self.save_books_to_file(filename)
            print("Books File has been saved.")

        elif choice == "4":
            filename = input("Enter the filename: ")
            self.load_books_from_file(filename)
            print("Books has been loaded.")

        elif choice == "5":
            exit()

#main
library = Library()

while True:
    library.transaction_menu()