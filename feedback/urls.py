# In feedback/urls.py (new file)
from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.custom_logout_view, name='custom_logout'),
]
