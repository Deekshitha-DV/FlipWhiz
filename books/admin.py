

# Register your models here.
# In books/admin.py
from django.contrib import admin
from .models import Book

admin.site.register(Book)