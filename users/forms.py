# This is the complete, correct, and final content for users/forms.py
"""Forms for the users application, including the user sign-up form."""

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    """
    A custom user creation form that includes the email field.

    Inherits from Django's base UserCreationForm and adds the 'email'
    field to the sign-up process.
    """

    class Meta(UserCreationForm.Meta):
        """Meta options for the CustomUserCreationForm."""

        model = User
        # By default, only username and password fields are shown.
        # We add 'email' to this tuple.
        fields = ("username", "email")