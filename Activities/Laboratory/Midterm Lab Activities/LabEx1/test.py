    def delete_book(self, book_id : str) -> None:
        if not book_id:
            print(">>> FIELD 'BOOK ID' IS EMPTY")
            return

        deleted_books = []
        with open(self.data_path, "r") as external_file:
            entries = external_file.readlines()

        new_external_data = []
        for entry in entries:
            entry_parts = entry.strip().split(",")
            if entry_parts[2] != book_id:
                new_external_data.append(entry)
            else:
                title, author, _, location = entry_parts
                deleted_books.append(English_Book(title, author, book_id, location))

        with open(self.data_path, "w") as external_file:
            external_file.writelines(new_external_data)

        for deleted_book in deleted_books:
            self.books = [book for book in self.books if book.get_book_id() != deleted_book.get_book_id()]