#from django.db import router
from django.urls import path
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
]
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')