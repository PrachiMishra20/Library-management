from utils import books

def add():
    name = input("Enter book name: ").upper()

    if name in books:
        print("Book already exists")
    else:
        books[name] = "AVAILABLE"
        print("Book added")