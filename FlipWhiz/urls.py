"""
URL configuration for FlipWhiz project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# At the top of FlipWhiz/urls.py
from django.views.generic.base import RedirectView

from django.conf import settings
from django.conf.urls.static import static


# New, corrected version
urlpatterns = [
    path('admin/', admin.site.urls),
    path('library/', include('books.urls')),  # <-- CHANGE THIS LINE
    path('', RedirectView.as_view(url='library/', permanent=False)), #
]


# FlipWhiz/urls.py (bottom part)

# This is only needed for development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)