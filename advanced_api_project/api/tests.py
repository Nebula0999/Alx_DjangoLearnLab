from django.test import TestCase
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

# Create an Author instance
author = Author.objects.create(name="J.K. Rowling")

# Create Book instances
book1 = Book.objects.create(title="Harry Potter and the Philosopher's Stone", publication_year=1997, author=author)
book2 = Book.objects.create(title="Harry Potter and the Chamber of Secrets", publication_year=1998, author=author)

# Serialize the Author instance with nested books
author_serializer = AuthorSerializer(author)
print(author_serializer.data)

# Test validation in BookSerializer
from rest_framework.exceptions import ValidationError
try:
    invalid_book = BookSerializer(data={
        'title': "Future Book",
        'publication_year': 3000,
        'author': author.id
    })
    invalid_book.is_valid(raise_exception=True)
except ValidationError as e:
    print(e)
# Create your tests here.
