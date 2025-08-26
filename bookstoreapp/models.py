from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="books"   # -> author.books.all()
    )
    categories = models.ManyToManyField(
        Category,
        related_name="books"   # -> category.books.all()
    )

    def __str__(self):
        return self.title
