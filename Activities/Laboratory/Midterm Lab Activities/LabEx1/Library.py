from Book import BookType
import os


class Library:
    def __init__(self,filename, mode = "r"):
        self.file = open(filename,mode) 
        self.books = []
        self.borrows = []
    
    def closeFile(self):
        self.file.close()
    
    def addBook(self, title, author, bookId, subject, shelf,filename = "library.txt"):
        file = open(filename, "a")
        file.write(f"{title},{author},{bookId},{subject},{shelf}\n")
        file.close()
        self.books.append(BookType(title,author,bookId,subject,shelf))
        print("\nADDED BOOK INFORMATION")
        print(f"Title: {title}\nAuthor: {author}\nBook Id number: {bookId}\nBook Type: {subject}\nShelf: {shelf}\n")
        
        
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
                break
            
        file = open("library.txt","w")  
        for book in self.books:
            file.write(f"{book.title},{book.author},{book.getBookId()},{book.subject},{book.shelf}\n")
        file.close()
                         
    def borrowBook(self, bookId):
        def borrowBookFunc():
            for book in self.books:
                if book.getBookId() == bookId:
                    self.borrows.append(BookType(book.title,book.author,book.getBookId(),book.subject,book.shelf))
                    self.books.remove(book)
                    print("\nBORROWED BOOK INFORMATION")
                    print(f"Title: {book.title}\nAuthor: {book.author}\nBook Id number: {book.getBookId()}\nBook Type: {book.subject}\nShelf: {book.shelf}\n")
                    break
            file = open("library.txt","w")  
            for book in self.books:
                file.write(f"{book.title},{book.author},{book.getBookId()},{book.subject},{book.shelf}\n")
            file.close() 

            file = open("borrow.txt","a")
            for book in self.borrows:
                file.write(f"{book.title},{book.author},{book.getBookId()},{book.subject},{book.shelf}\n")
            file.close()

        if os.path.exists("borrow.txt"):
            borrowBookFunc()
        else:
            file = open("borrow.txt","x")
            file.close()
            borrowBookFunc()

    def returnBook(self,bookId):
        for book in self.borrows:
            if book.getBookId() == bookId:
                self.books.append(BookType(book.title,book.author,book.getBookId(),book.subject,book.shelf))
                self.borrows.remove(book)
                print("\nRETURNED BOOK INFORMATION")
                print(f"Title: {book.title}\nAuthor: {book.author}\nBook Id number: {book.getBookId()}\nBook Type: {book.subject}\nShelf: {book.shelf}\n")
                break
        
        file = open("library.txt","w")  
        for book in self.books:
            file.write(f"{book.title},{book.author},{book.getBookId()},{book.subject},{book.shelf}\n")
        file.close() 

        file = open("borrow.txt","w")
        if not self.borrows:
            file.write("")
        else:
            for book in self.borrows:
                file.write(f"{book.title},{book.author},{book.getBookId()},{book.subject},{book.shelf}\n")
        file.close() 

    def displayAllBooks(self):
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, Book Id number: {book.getBookId()}, Book Type: {book.subject}, Shelf: {book.shelf}") 
        print("")
    

    def displayShelves(self):
        shelf = input("\nPlease enter the shelf you want to see: ")
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
            case _:
                print("Invalid Input")
        print("")
    
    def displayAllSubjects(self):
        subject = input("Please select the subject of the books you want to see: ")
        match subject.lower():
            case "english":
                print("These are the books in the English subject.")
                for book in self.books:
                    if book.subject == "English":
                        print(f"Title: {book.title}, Author: {book.author}, Book Id number: {book.getBookId()}, Shelf: {book.shelf}") 
            case "math":
                print("These are the books in the Math subject.")
                for book in self.books:
                    if book.subject == "Math":
                        print(f"Title: {book.title}, Author: {book.author}, Book Id number: {book.getBookId()}, Shelf: {book.shelf}") 
            case "filipino":
                print("These are the books in the Filipino subject.")
                for book in self.books:
                    if book.subject == "Filipino":
                        print(f"Title: {book.title}, Author: {book.author}, Book Id number: {book.getBookId()}, Shelf: {book.shelf}") 
            case "science":
                print("These are the books in the Science subject.")
                for book in self.books:
                    if book.subject == "Science":
                        print(f"Title: {book.title}, Author: {book.author}, Book Id number: {book.getBookId()}, Shelf: {book.shelf}") 
            case "history":
                print("These are the books in the History subject.")
                for book in self.books:
                    if book.subject == "History":
                        print(f"Title: {book.title}, Author: {book.author}, Book Id number: {book.getBookId()}, Shelf: {book.shelf}")
            case _:
                print("Invalid subject")
        print("") 


    def displayById(self):
        bookId = input("Please Enter the book ID: ")
        print(f"These are the book with the book ID: {bookId}")
        for book in self.books:
            if book.getBookId() == bookId:
                print(f"Title: {book.title}, Author: {book.author}, Book Type: {book.subject}, Shelf: {book.shelf}")
        print("")

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
    
    def help(self):
        print("Here are some of the commands to help you use the Library program")
        print("add: add a book")
        print("delete: delete a book")
        print("borrow: borrow a book")
        print("return: return a book")
        print("show all: display all books in the library")
        print("show shelf: display all books in a shelf")
        print("show by subject: display all books of a particular subject")
        print("show by ID: display the book with the selected book ID")
        print("help: shows all the commands")
        print("exit: exit the program\n")


    
