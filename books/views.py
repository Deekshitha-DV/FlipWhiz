# This is the complete, correct, and final content for books/views.py
"""Views for handling the book library, details, favorites, and categories."""

import json
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Book, Category, Favorite
from django.http import StreamingHttpResponse
from django.conf import settings
from elevenlabs.client import ElevenLabs
import PyPDF2


def book_list(request, category_slug=None):
    """
    Display a list of all books, optionally filtered by category.
    This view also prepares book data as a JSON object for the frontend.
    """
    category = None
    categories = Category.objects.all()
    books = Book.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        books = books.filter(category=category)

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
            favorite.delete()

        return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))


@login_required
def favorite_list(request):
    """Display a list of the current user's favorite books."""
    favorite_books = Book.objects.filter(favorite__user=request.user)

    books_data = []
    for book in favorite_books:
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
        "is_favorites_page": True, # Flag to tell the template this is the favorites page
    }
    return render(request, "books/book_list.html", context)


@login_required
def listen_to_book(request, pk):
    """
    Extracts text from a book's PDF and streams the audio using ElevenLabs.
    """
    book = get_object_or_404(Book, pk=pk)

    try:
        # --- 1. Extract Text from PDF ---
        text_to_read = ""
        with open(book.ebook_file.path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text_to_read += page.extract_text() + " "
        
        # Clean up text a bit
        text_to_read = text_to_read.replace('\n', ' ').strip()
        
        if not text_to_read:
            # Handle case where no text could be extracted
            raise ValueError("Could not extract text from the PDF.")

        # --- 2. Call ElevenLabs API ---
        client = ElevenLabs(api_key=settings.ELEVENLABS_API_KEY)
        
        # We use a generator to stream the audio chunk by chunk
        audio_stream = client.generate(
            text=text_to_read[:4000], # Limit to first 4000 chars for free tier
            voice="Rachel", # A high-quality pre-built voice
            model="eleven_multilingual_v2",
            stream=True
        )

        # --- 3. Stream the Audio to the Browser ---
        response = StreamingHttpResponse(audio_stream, content_type='audio/mpeg')
        return response

    except Exception as e:
        # Handle errors gracefully (e.g., file not found, API error)
        # In a real app, you'd return a proper error message
        print(f"An error occurred: {e}")
        return StreamingHttpResponse(status=500)