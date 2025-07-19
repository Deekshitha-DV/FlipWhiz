# This is the complete, correct, and final content for books/models.py
"""Database models for the books application."""

from django.db import models
from django.conf import settings # Use settings for AUTH_USER_MODEL
from django.contrib.auth.models import User # Kept for compatibility if needed elsewhere


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


class UserBookStatus(models.Model):
    """Links a User to a Book and stores their interaction status."""

    # Define the possible statuses using a ChoiceField
    STATUS_CHOICES = [
        ('FAVORITE', 'Favorite'),
        ('READ_NEXT', 'Reading List'),
        ('COMPLETED', 'Completed'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta options for the UserBookStatus model."""
        # A user can only have one status per book
        unique_together = ('user', 'book')

    def __str__(self):
        """Return the string representation of the status."""
        return f"{self.user.username} - {self.book.title}: {self.get_status_display()}"