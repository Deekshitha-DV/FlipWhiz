from django.shortcuts import render


# Create your views here.
# In users/views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login') # Redirect to login page after successful sign-up
    template_name = 'registration/signup.html'