from utils import books

def return_book():
    name = input("Enter book name: ").upper()

    if name in books:
        if books[name] == "AVAILABLE":
            print("Book already available")
        else:
            books[name] = "AVAILABLE"
            print("Book returned")
    else:
        print("Book not found")