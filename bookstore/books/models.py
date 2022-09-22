from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.CharField(max_length=200)
    publication_year = models.PositiveIntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=5)

    def __str__(self):
        return str(self.title) + " by " + str(self.author)

class BookStore(models.Model):
    books = models.ManyToManyField(Book)