from django.contrib import admin
from .models import Book, BookStore

# Register your models here.
admin.site.register(Book)
admin.site.register(BookStore)