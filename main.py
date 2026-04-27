from add_books import add
from show_books import show
from issue_books import issue
from return_books import return_book

while True:
    print("\n-----library menu-----")
    print("1.add book")
    print("2.show book")
    print("3.issue book")
    print("4.return book")
    print("exit")

    ch = input("Enter choice:")

    if ch=="1":
        add()
    elif ch == "2":
        show()
    elif ch == "3":
        issue()
    elif ch == "4":
        return_book()
    elif ch == "5":
        print("Thank you")
        break
    else:
        print("Invalid choice")
    

