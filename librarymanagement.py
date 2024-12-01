#library management system 

class Book:
    def __init__(self, bookId, title, author):
        self.bookId = bookId ; self.author = author ; self.title = title ; self.is_issued = False
        
    def __str__(self):
        if self.is_issued==True:
            status="issued"
        else:
            status="available"
        return "ID: " + str(self.bookId) + ", Title: " + self.title + ", Author: " + self.author + ", Status: " + status


class Library:
    def __init__(self):
        self.books = []

    def addBook(self, bookId, title, author):
        newBook = Book(bookId, title, author)
        self.books.append(newBook)
        print("we have added the book successfully")

    def viewBooks(self):
        if (not self.books):
            print("library is empty at this point")
            return
        print("\nBooks available in the library:")
        for book in self.books:
            print(book)

    def issueBook(self, bookId):
        for book in self.books:
            if book.bookId == bookId:
                if book.is_issued:
                    print("Book is not available and is already issued")
                else:
                    book.is_issued = True
                    print("Book issued successfully!")
                return
        print(f"Book with ID {bookId} is not found in our library.")

    def returnBook(self, bookId):
        for book in self.books:
            if book.bookId == bookId:
                if not book.is_issued:
                    print("Book was not issued in our library")
                else:
                    book.is_issued = False
                    print("Book is returned successfully!")
                return
        print(f"Book with ID {bookId} not found.")


def main():
    library = Library()

    while True:
        print("Library Management System")
        print("please enter your request")
        print("Add Book")
        print("View Books")
        print("Issue Book")
        print("Return Book")
        print("Exit")
        your_input=int(input("please enter your choice"))

        if your_input== 1:
            bookId = int(input("please enter your BookId "))
            title = input(" please enter the Book Title ")
            author = input("please enter the Book author ")
            library.addBook(bookId, title, author)

        elif your_input == 2:
            library.viewBooks()

        elif your_input == 3:
            bookId = int(input("please enter Book ID that you want to issue"))
            library.issueBook(bookId)

        elif your_input == 4:
            bookId = int(input("please enter Book ID that you want to return: "))
            library.returnBook(bookId)

        elif your_input == 5:
            print("we are exiting the system .")
            break

        else:
            print("Please enter a vaild choice ")


if __name__ == "__main__":
    main()
