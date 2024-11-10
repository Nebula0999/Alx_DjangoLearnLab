from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = author.books.all()
    return books

# List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books

# Retrieve the librarian for a library
def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.name
    return librarian

if __name__ == "__main__":
    author_books = books_by_author("Author Name")
    for book in author_books:
        print(f"Book by Author: {book.title}")

    library_books = books_in_library("Library Name")
    for book in library_books:
        print(f"Book in Library: {book.title}")

    librarian = librarian_for_library("Library Name")
    print(f"Librarian: {librarian.name}")