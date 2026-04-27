def add_book():
    book_name=input("Enter book name:").upper()
    books.append(book_name)
    print(f"Book{book_name}added.")