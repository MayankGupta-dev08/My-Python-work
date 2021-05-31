class Library:

    def __init__(self, listofBooks):
        self.books = listofBooks
        self.givenBooks = []

    def showAvailableBooks(self):
        print("Books present in this library are: ")
        for i, book in enumerate(self.books):
            print(f"{i+1}. {book}")

    def borrowBooks(self, bookName):
        if bookName in self.books:
            print(f"Congrats!! The book - {bookName} is available and it's been issued to you.")
            print(f"Please keep ot safe and return within 30 days.")
            self.books.remove(bookName)
            self.givenBooks.append(bookName)
            return True
        else:
            print("Sorry, this book is either not available or already been issued to someone else.\nPlease wait untill it's returned or choose another book.")
            return False

    def returnBooks(self, bookName):
        if bookName in self.givenBooks:
            print(f"Hope you have enjoyed reading {bookName} book.\nThanks for returning it!")
            self.books.append(bookName)
            self.givenBooks.remove(bookName)
        else:
            print("You haven't Borrowed this book from here, but if you want you can donate this book.\n For DONATION, choose option (4) from main menu.")

    def addBooks(self, bookName):
        print("Thanks for your kind gesture!\nAdding a book to Central Library..........")
        self.books.append(bookName)


class Student:

    def requestBooks(self):
        self.reqBook = input("Enter name of the book you want to borrow: ")
        return self.reqBook

    def returnBooks(self):
        self.retBook = input("Enter name of the book you want to return: ")
        if (self.retBook.startswith(" ") or self.retBook.startswith("@") or self.retBook.startswith("#") or self.retBook.startswith("!") or self.retBook.startswith("&") or self.retBook.startswith("$") or self.retBook.startswith("^") or self.retBook.startswith("~") or self.retBook.startswith("%")):
            print("Make sure Book name doesn't start with space or (!, @, #, &, $, %, ^, ~)")
            self.returnBooks()
        else:
            return self.retBook

    def donateBooks(self):
        self.dotBook = input("Please enter name of the book you want to donate: ")
        if (self.retBook.startswith(" ") or self.retBook.startswith("@") or self.retBook.startswith("#") or self.retBook.startswith("!") or self.retBook.startswith("&") or self.retBook.startswith("$") or self.retBook.startswith("^") or self.retBook.startswith("~") or self.retBook.startswith("%")):
            print("Make sure Book name doesn't start with space or (!, @, #, &, $, %, ^, ~)")
            self.donateBooks()
        else:
            print("Thanks for your donation, have a great day ahead!!")
            return self.dotBook


if __name__ == "__main__":
    centraLibrary = Library(["C", "C++", "Java", "Python", "Data Structures", "Algorithms", "Django", "Java Script", "Machine Learning", "Data Science", "Flask", "Panda", "Numpy", "HTML"])
student = Student()
while True:
    try:
        welcomeMessage = '''\n~~~~~~~~~~WELCOME TO CENTRAL LIBRARY~~~~~~~~~~
        1.  Show all available books
        2.  Borrow a book
        3.  Return a book
        4.  Donate a book
        5.  Exit the Library\n'''
        print(welcomeMessage)
        choice = int(input("Enter your choice: "))
        if choice == 1:
            centraLibrary.showAvailableBooks()
        elif choice == 2:
            centraLibrary.borrowBooks(student.requestBooks())
        elif choice == 3:
            centraLibrary.returnBooks(student.returnBooks())
        elif choice == 4:
            centraLibrary.addBooks(student.donateBooks())
        elif choice == 5:
            print("Thanks for using Central Library, hope you had a great time.")
            exit()
        else:
            print("Invalid choice entered!!")
    except Exception as e:
        print("Make sure you enter a number!!")
