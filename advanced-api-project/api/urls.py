from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),  # List all books
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),  # Book details by ID
    path('books/create/', BookCreateView.as_view(), name='book-create'),  # Add a new book
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),  # Update a book
    path('books/delete/', BookDeleteView.as_view(), name='book-delete'),  # Delete a book
    path("books/update", BookDeleteView.as_view(), name='book-delete'),  # Delete a book
]