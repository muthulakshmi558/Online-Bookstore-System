from django.shortcuts import render, get_object_or_404
from .models import Book, Author, Category
def home(request):
    return render(request, "bookstoreapp/home.html")
def book_list(request):
    books = Book.objects.select_related("author").prefetch_related("categories").all()
    return render(request, "bookstoreapp/book_list.html", {"books": books})

def author_books(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    books = author.books.all()
    return render(request, "bookstoreapp/author_books.html", {"author": author, "books": books})

def category_books(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    books = category.books.all()
    return render(request, "bookstoreapp/category_books.html", {"category": category, "books": books})
