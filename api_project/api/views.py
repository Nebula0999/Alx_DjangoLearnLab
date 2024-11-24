from django.shortcuts import render
from rest_framework import generics, viewsets
from .serializers import BookSerializer
from .models import Book
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsEditor

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated(), IsEditor()]  # Only Editors can create books
        elif self.action in ['update', 'partial_update']:
            return [IsAuthenticated(), IsAdminUser()]  # Only Admin users can edit books
        else:
            return [IsAuthenticated()] 




# Create your views here.
