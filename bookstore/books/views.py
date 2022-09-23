from django.shortcuts import render
from rest_framework import viewsets, routers, serializers, status, filters
from rest_framework.response import Response
from .models import Book, BookStore
from .serializers import BookSerializer, BookStoreSerializer, UserSerializer
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
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

class UserViewSet(viewsets.ModelViewSet):
    """
    List all users, or create a new user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
