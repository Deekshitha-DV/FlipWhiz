# This is the complete, correct, and final content for books/models.py
"""Database models for the books application."""

from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """Represents a book category (e.g., Fiction, Science)."""

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        """Meta options for the Category model."""

        verbose_name_plural = "Categories"

    def __str__(self):
        """Return the string representation of the Category."""
        return self.name


class Book(models.Model):
    """Represents a single e-book in the library."""

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )
    description = models.TextField()
    cover_image = models.ImageField(upload_to="book_covers/")
    ebook_file = models.FileField(upload_to="ebook_files/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the string representation of the Book."""
        return self.title


class Favorite(models.Model):
    """Links a User to a Book they have favorited."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta options for the Favorite model."""

        # This constraint ensures a user can't favorite the same book more than once
        unique_together = ("user", "book")

    def __str__(self):
        """Return the string representation of the Favorite relationship."""
        return f"{self.user.username}'s favorite: {self.book.title}"