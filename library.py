from books import Books


class Library(Books):
    def __init__(self):
        self.books = []

    def add_book_toLibrary(self, book):
        self.books.append(book)

    def remove_book_fromLibrary(self, book):
        self.books.remove(book)
        print(book.title, "book has been removed from library")

    def display_availableBooks(self):
        print("Book Title", "\t\t\t", "Author")
        for book in self.books:
            print(book.title, "\t", book.author)
        print("---------------------------------------------")


# create object of parent class i.e, Books and add title and author for the book/s
book_obj1 = Books("Java Programming", "James Gosling")
book_obj2 = Books("Python Programming", "Guido van Rossum")
book_obj3 = Books("Performance Testing", "Ian Molyneaux")

# create object of child class i.e, Library
library_obj = Library()

# Call add method using library class object to add the books into Library
library_obj.add_book_toLibrary(book_obj1)
library_obj.add_book_toLibrary(book_obj2)
library_obj.add_book_toLibrary(book_obj3)

# Call display method from Library object to display the available books into Library
print("List of available books in the library")
library_obj.display_availableBooks()

# Call remove method using library class object to remove one of the book from library
library_obj.remove_book_fromLibrary(book_obj3)

# Then call display method using Library object to display the available books in the library
print("List of available books in the library")
library_obj.display_availableBooks()
