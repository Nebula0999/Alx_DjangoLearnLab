#from django.db import router
from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
    path('', include('api.urls'))
]
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')