#from django.db import router
from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
    path('', include('router.urls'))
    path('api/token/', obtain_auth_token, name='api_token_auth'),  # Endpoint to get tokens
]
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')


