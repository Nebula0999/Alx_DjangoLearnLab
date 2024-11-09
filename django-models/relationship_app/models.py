from django.db import models


class Author(models.Model):
    author_name = models.CharField(max_length=20)

class Book(models.Model):
    title = models.CharField(max_length=20)
    author = models.ForeignKey(Author)

class Library(models.Model):
    library_name = models.CharField(max_length=20)
    books = models.ManyToManyField(Book)

class Librarian(models.Model):
    librarian_name = models.CharField(max_length=20)
    library = models.OneToOneField(Library)

# Create your models here.
