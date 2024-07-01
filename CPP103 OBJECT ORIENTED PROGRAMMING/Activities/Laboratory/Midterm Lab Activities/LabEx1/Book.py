class Book:
    def __init__(self,title,author,bookId):
        self.title = title
        self.author = author
        self.__bookId = bookId

    def getBookId(self):
        return self.__bookId
    
    def setBookId(self,bookId):
        self.__bookId = bookId
    
class BookType(Book):
    def __init__(self,title,author,bookId,subject,shelf):
        super().__init__(title,author,bookId) 
        self.subject = subject
        self.shelf = shelf