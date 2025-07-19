# This is the complete, correct, and final content for books/views.py

import json
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Book, Category, UserBookStatus

# In books/views.py

def book_list(request, category_slug=None):
    """
    Display a list of books, optionally filtered by category.
    This view also prepares book data as a JSON object for the frontend.
    """
    category = None
    categories = Category.objects.all()
    
    # Start with all books
    books = Book.objects.all()

    # --- THIS IS THE CRITICAL FILTERING LOGIC ---
    if category_slug:
        # If a category slug is provided in the URL, filter the books
        category = get_object_or_404(Category, slug=category_slug)
        books = books.filter(category=category)
    # --- END OF CRITICAL LOGIC ---

    # Prepare the (now correctly filtered) book data for JavaScript
    books_data = []
    for book in books:
        books_data.append({
            "title": book.title,
            "author": book.author,
            "cover_image_url": book.cover_image.url if book.cover_image else None,
            "detail_url": reverse("book_detail", args=[book.pk]),
            "category": {"name": book.category.name} if book.category else None,
        })

    # This part handles the close-book animation after logout
    just_logged_out = request.session.pop('just_logged_out', False)
    
    context = {
        "books_json": json.dumps(books_data),
        "categories": categories,
        "current_category": category,
        "session_data": json.dumps({'just_logged_out': just_logged_out})
    }
    return render(request, "books/book_list.html", context)


def book_detail(request, pk):
    """Display the details for a single book and its status for the current user."""
    book = get_object_or_404(Book, pk=pk)
    current_status = None
    if request.user.is_authenticated:
        status_obj = UserBookStatus.objects.filter(user=request.user, book=book).first()
        if status_obj:
            current_status = status_obj.status
    context = {"book": book, "current_status": current_status}
    return render(request, "books/book_detail.html", context)


class SetBookStatusView(LoginRequiredMixin, View):
    """Handle POST requests to set or update a book's status for a user."""

    def post(self, request, pk):
        """Set or update a book's status based on the submitted form."""
        book = get_object_or_404(Book, pk=pk)
        status_to_set = request.POST.get('status')
        valid_statuses = [choice[0] for choice in UserBookStatus.STATUS_CHOICES]
        if status_to_set not in valid_statuses:
            return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))
        status_obj = UserBookStatus.objects.filter(user=request.user, book=book).first()
        if status_obj:
            if status_obj.status == status_to_set:
                status_obj.delete()
            else:
                status_obj.status = status_to_set
                status_obj.save()
        else:
            UserBookStatus.objects.create(
                user=request.user, book=book, status=status_to_set
            )
        return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))

# You can keep your favorite_list view as it was, or update its query
@login_required
def favorite_list(request):
    """Display a list of the current user's favorite books."""
    favorite_books = Book.objects.filter(userbookstatus__user=request.user, userbookstatus__status='FAVORITE')
    books_data = []
    for book in favorite_books:
        books_data.append({
            'title': book.title,
            'author': book.author,
            'cover_image_url': book.cover_image.url if book.cover_image else None,
            'detail_url': reverse('book_detail', args=[book.pk]),
            'category': {'name': book.category.name} if book.category else None,
        })
    context = {
        'books_json': json.dumps(books_data),
        'is_favorites_page': True,
    }
    return render(request, "books/book_list.html", context)