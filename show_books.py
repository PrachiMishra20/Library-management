from utils import books

def show_book():
    if len(books) == 0:
        print("No books available")
    else:
        print("\n Book List:")
        for name in books:
            print(name, "-", books[name])
                                   