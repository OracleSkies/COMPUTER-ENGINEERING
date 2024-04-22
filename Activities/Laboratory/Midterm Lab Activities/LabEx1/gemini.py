from Book import BookType
from icecream import ic


class Library:
  def __init__(self, filename, mode="r"):
    self.file = open(filename, mode)
    self.books = []

  def close_file(self):
    self.file.close()

  def add_book(self, title, author, book_id, subject, shelf, filename="library.txt"):
    file = open(filename, "a")
    file.write(f"{title},{author},{book_id},{subject},{shelf}\n")
    file.close()

    self.books.append(BookType(title, author, book_id, subject, shelf))
    print("Book successfully added")

  def load_book(self, filename):
    file = open(filename, "r")
    for book in file:
      title, author, book_id, subject, shelf = book.strip().split(",")
      self.books.append(BookType(title, author, book_id, subject, shelf))
    file.close()

  def delete_book(self, filename, line_number):
    # Implement logic to delete book from file and list based on line number

  def borrow_book(self):
    # Implement book borrowing logic

  def return_book(self):
    # Implement book return logic

  def display_books(self, filter_by=None, filter_value=None):
    self.load_book("library.txt")  # Load books directly

    if not self.books:
      print("No books found.")
      return

    for book in self.books:
      if filter_by and filter_value:
        if getattr(book, filter_by) == filter_value:  # Use getattr for dynamic attribute access
          print(
              f"Title: {book.title}, Author: {book.author}, Book Id number: {book.get_book_id()}, Book Type: {book.subject}, Shelf: {book.shelf}"
          )
      else:
        print(
            f"Title: {book.title}, Author: {book.author}, Book Id number: {book.get_book_id()}, Book Type: {book.subject}, Shelf: {book.shelf}"
        )

  def display_shelves(self):
    shelves = ["A", "B", "C", "D", "E"]
    while True:
      print("\nPlease enter the shelf you want to see: ")
      shelf_choice = input().lower()
      if shelf_choice in shelves:
        self.display_books(filter_by="shelf", filter_value=shelf_choice)
        break
      elif shelf_choice == "exit":
