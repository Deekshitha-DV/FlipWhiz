# This is the complete, correct, and final content for FlipWhiz/urls.py

"""
Main URL configuration for the FlipWhiz project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

# We import Django's built-in LoginView for our login page.
from django.contrib.auth import views as auth_views

urlpatterns = [
    # 1. Admin Panel URL
    path('admin/', admin.site.urls),

    # 2. Authentication URLs
    # We now define them explicitly to allow for our custom logout.
    path(
        'accounts/login/',
        auth_views.LoginView.as_view(template_name='registration/login.html'),
        name='login'
    ),
    # This includes our custom sign-up URL from the 'users' app.
    path('accounts/', include('users.urls')),
    # This includes our custom logout/feedback URL from the 'feedback' app.
    path('accounts/', include('feedback.urls')),

    # 3. Main Application URLs
    # This includes all URLs for the book library, details, favorites, etc.
    path('library/', include('books.urls')),

    # 4. Homepage Redirect
    # Redirects the root URL ('/') to our main library page.
    path('', RedirectView.as_view(url='library/', permanent=False)),
]

# This block is for serving media files (like book covers) during development.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)