# Register your models here.
# In books/admin.py
from django.contrib import admin
from .models import Book

from .models import Book, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)} # Auto-fills the slug from the name!

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category') # Add category to the list
    list_filter = ('category',) # Add a filter sidebar for categories