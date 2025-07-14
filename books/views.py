# This is the complete, correct, and final content for books/views.py
"""Views for handling the book library, details, and favorites."""

import json
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book, Category, Favorite


def book_list(request, category_slug=None):
    """
    Display a list of books, optionally filtered by category.
    This view also prepares book data as a JSON object for the frontend.
    """
    category = None
    categories = Category.objects.all()
    books = Book.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        books = books.filter(category=category)

    # Prepare data in a format safe for JavaScript (JSON)
    books_data = []
    for book in books:
        books_data.append(
            {
                "title": book.title,
                "author": book.author,
                "cover_image_url": book.cover_image.url if book.cover_image else None,
                "detail_url": reverse("book_detail", args=[book.pk]),
                "category": {"name": book.category.name} if book.category else None,
            }
        )

    context = {
        "books_json": json.dumps(books_data),
        "categories": categories,
        "current_category": category,
    }
    return render(request, "books/book_list.html", context)


def book_detail(request, pk):
    """Display the details for a single book and its favorite status."""
    book = get_object_or_404(Book, pk=pk)
    is_favorite = False
    if request.user.is_authenticated:
        # Check if a Favorite object exists for this user and book
        is_favorite = Favorite.objects.filter(user=request.user, book=book).exists()

    context = {"book": book, "is_favorite": is_favorite}
    return render(request, "books/book_detail.html", context)


class AddToFavoritesView(LoginRequiredMixin, View):
    """Handle POST requests to add or remove a book from favorites."""

    def post(self, request, pk):
        """Add or remove a book from the current user's favorites."""
        book = get_object_or_404(Book, pk=pk)
        favorite, created = Favorite.objects.get_or_create(
            user=request.user, book=book
        )

        if not created:
            # If the favorite already existed, delete it.
            favorite.delete()

        # Redirect back to the page the user was on
        return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))