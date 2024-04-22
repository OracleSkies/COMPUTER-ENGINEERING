from Book import BookType
from icecream import ic
import os


class Library:
    def __init__(self,filename, mode = "r"):
        self.file = open(filename,mode) 
        self.books = []
    
    def closeFile(self):
        self.file.close()
    
    def addBook(self, title, author, bookId, subject, shelf,filename = "library.txt"):
        file = open(filename, "a")
        file.write(f"{title},{author},{bookId},{subject},{shelf}\n")
        self.books.append(BookType(title,author,bookId,subject,shelf))
        print("book successfully added")
        
    def loadBook(self,filename):
        file = open(filename,"r")
        for book in file:
            title, author, bookId, subject, shelf = book.strip().split(",")
            self.books.append(BookType(title, author, bookId, subject, shelf))
        file.close()

    def deleteBook(self,bookId):
        for book in self.books:
            if book.getBookId() == bookId:
                self.books.remove(book)
                print("remove successful")
        return

    def borrowBook(self):
        pass
    def returnBook(self):
        pass

    def displayAllBooks(self):
        def displayLoop():
            for book in self.books:
                print(f"Title: {book.title}, Author: {book.author}, Book Id number: {book.getBookId()}, Book Type: {book.subject}, Shelf: {book.shelf}") 
        if not self.books: 
            self.loadBook("library.txt")
            displayLoop()
        else:
            displayLoop()

        
    def displayShelves(self):
        def displayLoop():
            while True:
                shelf = input("\nPlease enter the shelf you want to see: ")
                ic(shelf)
                match shelf.lower():
                    case "a":
                        print("These are the books in Shelf A")
                        for book in self.books:
                            if book.shelf == "A":
                                print(f"Title: {book.title}, Author: {book.author}, Book Id number: {book.getBookId()}, Book Type: {book.subject}")
                    case "b":
                        print("These are the books in Shelf B")
                        for book in self.books:
                            if book.shelf == "B":
                                print(f"Title: {book.title}, Author: {book.author}, Book Id number: {book.getBookId()}, Book Type: {book.subject}")
                    case "c":
                        print("These are the books in Shelf C")
                        for book in self.books:
                            if book.shelf == "C":
                                print(f"Title: {book.title}, Author: {book.author}, Book Id number: {book.getBookId()}, Book Type: {book.subject}")
                    case "d":
                        print("These are the books in Shelf D")
                        for book in self.books:
                            if book.shelf == "D":
                                print(f"Title: {book.title}, Author: {book.author}, Book Id number: {book.getBookId()}, Book Type: {book.subject}")
                    case "e":
                        print("These are the books in Shelf E")
                        for book in self.books:
                            if book.shelf == "E":
                                print(f"Title: {book.title}, Author: {book.author}, Book Id number: {book.getBookId()}, Book Type: {book.subject}")
                    case "exit":
                        break
                    case _:
                        print("Invalid Input")
        if not self.books:
            self.loadBook("library.txt")
            displayLoop()
        else:
            displayLoop()
    
    def displayAllSubjects(self):
        def displayLoop():
            while True:
                subject = input("Please select the subject of the books you want to see: ")
                match subject:
                    case "English":
                        print("These are the books in the English subject.")
                        for book in self.books:
                            if book.subject == "English":
                                print(f"Title: {book.title}, Author: {book.author}, Book Id number: {book.getBookId()}, Shelf: {book.shelf}") 
                    case "Math":
                        print("These are the books in the Math subject.")
                        for book in self.books:
                            if book.subject == "Math":
                                print(f"Title: {book.title}, Author: {book.author}, Book Id number: {book.getBookId()}, Shelf: {book.shelf}") 
                    case "Filipino":
                        print("These are the books in the Filipino subject.")
                        for book in self.books:
                            if book.subject == "Filipino":
                                print(f"Title: {book.title}, Author: {book.author}, Book Id number: {book.getBookId()}, Shelf: {book.shelf}") 
                    case "Science":
                        print("These are the books in the Science subject.")
                        for book in self.books:
                            if book.subject == "Science":
                                print(f"Title: {book.title}, Author: {book.author}, Book Id number: {book.getBookId()}, Shelf: {book.shelf}") 
                    case "History":
                        print("These are the books in the History subject.")
                        for book in self.books:
                            if book.subject == "History":
                                print(f"Title: {book.title}, Author: {book.author}, Book Id number: {book.getBookId()}, Shelf: {book.shelf}") 
        if not self.books:
            self.loadBook("library.txt")
            displayLoop()
        else:
            displayLoop()

    def displayById(self):
        def displayLoop():
            bookId = input("Please Enter the book ID: ")
            print(f"These are the book with the book ID: {bookId}")
            for book in self.books:
                if book.getBookId() == bookId:
                    print(f"Title: {book.title}, Author: {book.author}, Book Type: {book.subject}, Shelf: {book.shelf}")
        if not self.books:
            self.loadBook("library.txt")
            displayLoop()
        else:
            displayLoop()

    def chooseType(self):
        types = ["English", "Math", "Filipino", "Science","History"]
        while True:
            print("Select the type of book you want to add:")
            for bookType in types:
                print(bookType)
            choose = input("\nEnter the type of book you want to add: ")

            if choose in types:
                return choose
            else:
                print("Invalid type of book. Please try again.\n")
        
    def chooseShelf(self):
        shelves = ["A","B","C","D","E"]
        while True:
            print("Select the location\
                  \nwhere you want to put your book")
            for shelf in shelves:
                print(shelf)
            choose = input("\nSelect a shelf: ")
            if choose in shelves:
                return choose
            else:
                ("Invalid shelf. Please try again\n")

    
