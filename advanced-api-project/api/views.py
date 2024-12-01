from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from .permisssions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
# ListView for retrieving all books
class BookListView(generics.ListAPIView):
    """
    Retrieve a list of all books.
    Accessible to all users.
    """
    """
    Retrieve a list of all books with:
    - Filtering: Filter by title, author name, or publication year.
    - Searching: Perform full-text search on title and author name.
    - Ordering: Sort by title or publication year (ascending or descending).

    Examples:
    - Filtering: /books/?title=Harry Potter
    - Searching: /books/?search=Rowling
    - Ordering: /books/?ordering=-publication_year
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'author__name', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']

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
