from django.shortcuts import render
from rest_framework.response import Response 
from .models import Book
from .serializers import BookSerializer
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['POST'])
def bookCreate(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)