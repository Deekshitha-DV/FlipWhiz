# CORRECTED version of books/admin.py

from django.contrib import admin
from .models import Book, Category, UserBookStatus # <--
# 1. Import UserBookStatus instead of Favorite

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin view for the Category model."""
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Admin view for the Book model."""
    list_display = ("title", "author", "category", "uploaded_at")
    list_filter = ("category",)
    search_fields = ("title", "author")

@admin.register(UserBookStatus) # <--
# 2. Register the UserBookStatus model
class UserBookStatusAdmin(admin.ModelAdmin):
    """Admin view for the UserBookStatus model."""
    # 3. Update the display fields
    list_display = ("user", "book", "status", "added_on")
    list_filter = ("status", "user")