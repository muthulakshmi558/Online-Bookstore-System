from django.contrib import admin
from django.urls import path
from bookstoreapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("books/", views.book_list, name="book-list"),
    path("author/<int:author_id>/books/", views.author_books, name="author-books"),
    path("category/<int:category_id>/books/", views.category_books, name="category-books"),
]
