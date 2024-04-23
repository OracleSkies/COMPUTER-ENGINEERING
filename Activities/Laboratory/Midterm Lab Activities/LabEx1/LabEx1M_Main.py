import os
from Library import Library
#syntax: from [py filename] import [class in py file]

def transactionMenu():
    print("WELCOME TO THE LIBRARY!")
    library.help()
    while True:
        choice = input("Enter your action: ")
        match choice:
            case "add":
                title = input("Enter book title: ")
                author = input("Enter author: ")
                bookId = input("Enter book ID number: ")
                subject = library.chooseType()
                shelf = library.chooseShelf()
                library.addBook(title,author,bookId,subject,shelf)
                
            case "delete":
                bookId = input("Enter the Book ID that you want to delete: ")
                library.deleteBook(bookId)
            case "borrow":
                bookId = input("Enter the Book ID that you want to borrow: ")
                library.borrowBook(bookId)
            case "return":
                bookId = input("Enter the Book ID that you want to return: ")
                library.returnBook(bookId)
            case "show all":
                library.displayAllBooks()
            case "show shelf":
                library.displayShelves()
            case "show by subject":
                library.displayAllSubjects()
            case "show by ID":
                library.displayById()
            case "help":
                library.help()
            case"exit":
                break
            case _:
                print("Invalid action. Please try again")



if os.path.exists("library.txt"):
    library = Library("library.txt","r")
    library.loadBook("library.txt")
    transactionMenu()
else:
    file = open("library.txt","x")
    file.close()
    library = Library("library.txt","r")
    library.loadBook("library.txt")
    transactionMenu()




