from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from api.models import Author, Book

class BookAPITestCase(APITestCase):
    """
    Unit tests for the Book API endpoints.
    """

    @classmethod
    def setUpTestData(cls):
        # Create a user and authenticate
        cls.user = User.objects.create_user(username="testuser", password="testpass")
        cls.author = Author.objects.create(name="J.K. Rowling")

        # Create test data
        cls.book1 = Book.objects.create(title="Harry Potter and the Philosopher's Stone", publication_year=1997, author=cls.author)
        cls.book2 = Book.objects.create(title="Harry Potter and the Chamber of Secrets", publication_year=1998, author=cls.author)

    def test_list_books(self):
        """
        Test retrieving a list of books.
        """
        response = self.client.get("/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["title"], self.book1.title)

    def test_retrieve_book(self):
        """
        Test retrieving a single book by ID.
        """
        response = self.client.get(f"/books/{self.book1.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book1.title)

    def test_create_book_authenticated(self):
        """
        Test creating a book as an authenticated user.
        """
        self.client.login(username="testuser", password="testpass")
        data = {
            "title": "Harry Potter and the Prisoner of Azkaban",
            "publication_year": 1999,
            "author": self.author.id,
        }
        response = self.client.post("/books/create/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.last().title, "Harry Potter and the Prisoner of Azkaban")

    def test_create_book_unauthenticated(self):
        """
        Test creating a book as an unauthenticated user.
        """
        data = {
            "title": "Harry Potter and the Goblet of Fire",
            "publication_year": 2000,
            "author": self.author.id,
        }
        response = self.client.post("/books/create/", data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book(self):
        """
        Test updating an existing book.
        """
        self.client.login(username="testuser", password="testpass")
        data = {"title": "Harry Potter and the Sorcerer's Stone", "publication_year": 1997, "author": self.author.id}
        response = self.client.put(f"/books/{self.book1.id}/update/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Harry Potter and the Sorcerer's Stone")

    def test_delete_book(self):
        """
        Test deleting a book.
        """
        self.client.login(username="testuser", password="testpass")
        response = self.client.delete(f"/books/{self.book1.id}/delete/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books(self):
        """
        Test filtering books by title.
        """
        response = self.client.get("/books/?title=Harry Potter and the Chamber of Secrets")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], self.book2.title)

    def test_search_books(self):
        """
        Test searching books by a keyword.
        """
        response = self.client.get("/books/?search=Philosopher")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], self.book1.title)

    def test_order_books(self):
        """
        Test ordering books by publication year.
        """
        response = self.client.get("/books/?ordering=-publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], self.book2.title)