from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from .permisssions import IsAdminOrReadOnly

# ListView for retrieving all books
class BookListView(generics.ListAPIView):
    """
    Retrieve a list of all books.
    Accessible to all users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Read-only for unauthenticated users

# DetailView for retrieving a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieve details of a single book by its ID.
    Accessible to all users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# CreateView for adding a new book
class BookCreateView(generics.CreateAPIView):
    """
    Create a new book.
    Restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Restrict to authenticated users

    def perform_create(self, serializer):
        """
        Customize the save logic to add additional hooks.
        """
        serializer.save()  # Save the validated data

# UpdateView for modifying an existing book
class BookUpdateView(generics.UpdateAPIView):
    """
    Update an existing book.
    Restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# DeleteView for removing a book
class BookDeleteView(generics.DestroyAPIView):
    """
    Delete an existing book.
    Restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
# Create your views here.
