import os
from Library import Library
#syntax: from [py filename] import [class in py file]

def transactionMenu():
    while True:
        choice = input("Enter your choice: ")
        match choice:
            case "add":
                title = input("Enter book title: ")
                author = input("Enter author: ")
                bookId = input("Enter book ID number: ")
                subject = library.chooseType()
                shelf = library.chooseShelf()
                library.addBook(title,author,bookId,subject,shelf)
                
            case "delete":
                library.deleteBook()
            case "borrow":
                library.borrowBook()
            case "return":
                library.returnBook()
            case "display all":
                library.displayAllBooks()
            case "display shelf":
                library.displayShelves()
            case "show subject":
                library.displayAllSubjects()
            case "find book by ID":
                library.displayById()
            case"exit":
                break
            case _:
                print("Invalid action. Please try again")

if os.path.exists("library.txt"):
    library = Library("library.txt","r")
    transactionMenu()
else:
    file = open("library.txt","x")
    file.close()




