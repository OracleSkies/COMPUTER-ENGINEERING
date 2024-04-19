#Encapsulation
class Book:
    def __init__(self, title, author,bookId):
        self.title = title
        self.author = author
        self.bookId = bookId

#Inheritance
class EnglishBook(Book):
    def __init__(self, title, author, bookId, location):
        super().__init__(title, author, bookId)
        self.location = location

    def getBookInfo(self):
        print(f"Title: {self.title}, Author: {self.author}, ID: {self.bookId}, Location: {self.location}")

class Library:
    def __init__(self):
        self.books = []
#Abstraction
#Setters    
    def addBook(self, title, author, bookId, location):
        self.books.append(EnglishBook(title, author, bookId, location))

#Getters
    def getLibraryBooks(self):
        for book in self.books:
            print(book.getBookInfo())
    
    def saveBooksToFile(self,filename):
        file = open(filename, "a")
        
        #save the book to file (file handling)
        for book in self.books:
            file.write(f"{book.title},{book.author},{book.bookId},{book.location}\n")
        

    def loadBooksToFile(self,filename):
        file = open(filename,"r")
        for book in file:
            title, author, bookId, location = book.strip().split(",") #pwede pala to XD 
            self.books.append(EnglishBook(title, author, bookId, location))
        

    def transactionMenu(self):
        print("1. Add a book")
        print("2. View all books")
        print("3. Save books to file")
        print("4. Load books from file")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1": #pwedeng mag match case dito
            title = input("Enter book title: ")
            author = input("Enter author: ")
            bookId = input("Enter book ID: ")
            location = input("Enter location: ")

            self.addBook(title, author, bookId, location)
        elif choice == "2":
            self.getLibraryBooks() #ginamit ung getter
        elif choice == "3":
            filename = input("Enter the file name: ")
            self.saveBooksToFile(filename)
            print("Books File has been saved.")
        elif choice == "4":
            filename = input("Enter the file name to load: ")
            self.loadBooksToFile(filename)
            print("Books has been loaded")
        elif choice == "5":
            exit() #built in function
#main 
library = Library()
while True:
    library.transactionMenu()
