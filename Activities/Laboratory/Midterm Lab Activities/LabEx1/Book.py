class Book:
    def __init__(self,title,author,bookId):
        self.title = title
        self.author = author
        self.bookId = bookId
    
class BookType(Book):
    def __init__(self,title,author,bookId,subject,shelf):
        super().__init__(title,author,bookId)
        self.subject = subject
        self.shelf = shelf
    
    def getBookInfo(self):
        print(f"Title: {self.title}, Author: {self.author}, ID: {self.bookId}, Book Type: {self.subject}, Shelf: {self.shelf}")