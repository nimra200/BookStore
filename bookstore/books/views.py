from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response 
from .models import Book, BookStore
from .serializers import BookSerializer, BookStoreSerializer
from rest_framework.decorators import api_view

# Create your views here.
class BookStoreViewSet(viewsets.ModelViewSet):
    """
    List all the bookstores, or create a new bookstore.
    """
    queryset = BookStore.objects.all()
    serializer_class = BookStoreSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    List all books, or create a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer