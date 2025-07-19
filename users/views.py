# This is the complete, correct, and final content for users/views.py
"""Views for the users application, including sign-up and profile."""

from django.shortcuts import render
from django.urls import reverse_lazy

# NEW, correct import
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm
from books.models import UserBookStatus # Import the new model from the books app


class SignUpView(CreateView):
    """Handle user registration."""
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


@login_required
def profile_view(request):
    """Display the user's profile page with their bookshelves."""
    # Get all status objects for the current user in one query
    user_statuses = UserBookStatus.objects.filter(user=request.user)

    # Use list comprehensions to efficiently create lists for each shelf
    favorites = [
        status.book for status in user_statuses if status.status == 'FAVORITE'
    ]
    reading_list = [
        status.book for status in user_statuses if status.status == 'READ_NEXT'
    ]
    completed_books = [
        status.book for status in user_statuses if status.status == 'COMPLETED'
    ]

    context = {
        'favorites': favorites,
        'reading_list': reading_list,
        'completed_books': completed_books,
    }
    return render(request, 'users/profile.html', context)