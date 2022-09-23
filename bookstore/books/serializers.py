from rest_framework import serializers 
from .models import Book, BookStore


class BookStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookStore
        fields = '__all__'
        extra_kwargs = {'books': {'required': False}}

class BookSerializer(serializers.ModelSerializer):
    bookstores = BookStoreSerializer(many=True, read_only=True)
    class Meta:
        model = Book
        fields = ("id", "author", "title", "publication_year", "price", "bookstores")
        extra_kwargs = {'bookstores': {'required': False}}