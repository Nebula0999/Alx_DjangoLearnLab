from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Book, Author
from datetime import date

class BookSerializer(serializers.ModelSerializer)
    """
    Serializer for the Book model.
    Includes custom validation for the `publication_year` field.
    """
    class Meta:
        model = Book
        fields = "__all__"

        def validate_publication_year(self, value):
        #Validates the publication year
            current_year = date.today().year
            if value > current_year:
                raise serializers.ValidationError(f"Publication year cannot be in the future ({current_year}).")
            return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    Includes a nested serialization of books written by the author.
    """
    class Meta:
        model = Author
        fields = ['name']

