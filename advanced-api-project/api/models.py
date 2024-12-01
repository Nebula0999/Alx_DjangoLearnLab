from django.db import models

class Author(models.Model): #defines a model for Author
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Book(models.Model): #Defines a model for Book
    """
    Fields:
        title: Title of the book (string).
        publication_year: Year the book was published (integer).
        author: ForeignKey linking the book to its author (one-to-many relationship).
    """
    title = models.CharField(max_length=30)
    publication_year = models.IntegerField(unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# Create your models here.
