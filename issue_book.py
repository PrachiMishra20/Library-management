from utils import books

def issue():
    name = input("Enter book name: ").upper()

    if name in books:
        if books[name] == "ISSUED":
            print("Already issued")
        else:
            books[name] = "ISSUED"
            print("Book issued")
    else:
        print("Book not found")