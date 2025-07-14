# This is the complete, correct, and final content for books/admin.py
"""Admin panel configurations for the books application."""

from django.contrib import admin
from .models import Book, Category, Favorite


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin view for the Category model."""

    list_display = ("name", "slug")
    # Automatically creates the 'slug' from the 'name' field, which is very helpful.
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Admin view for the Book model."""

    # Displays these columns in the book list view
    list_display = ("title", "author", "category", "uploaded_at")
    # Adds a filter sidebar to easily find books by category
    list_filter = ("category",)
    # Adds a search bar to search for books by title or author
    search_fields = ("title", "author")


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    """Admin view for the Favorite model."""

    # Displays these columns in the favorite list view
    list_display = ("user", "book", "created_at")
    # Adds a filter sidebar for users and books
    list_filter = ("user", "book")