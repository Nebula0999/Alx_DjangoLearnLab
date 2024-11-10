from django.db import models
class Author(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=20)
    author = models.ForeignKey(Author)

    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=20)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=20)
    library = models.OneToOneField(Library)

    def __str__(self):
        return self.name