# In books/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # This will be our main library page showing all books
    path('', views.book_list, name='book_list'), 
    
    # This will handle the filtering, e.g., /library/category/fiction/
    path('category/<slug:category_slug>/', views.book_list, name='book_list_by_category'),
    
    # This is for the detail page, it remains the same
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
]