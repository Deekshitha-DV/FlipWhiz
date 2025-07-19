# This is the complete, correct, and final content for books/urls.py
"""URL patterns for the books application."""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('favorites/', views.favorite_list, name='favorite_list'),
    path('category/<slug:category_slug>/', views.book_list, name='book_list_by_category'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),

    # The URL for setting a book's status
    path(
        'book/<int:pk>/set-status/',
        views.SetBookStatusView.as_view(),
        name='set_book_status'
    ),
]