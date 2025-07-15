from django.db import models

# Create your models here.
# In feedback/models.py (the one inside the 'feedback' app)

from django.conf import settings # Use settings for the user model

class Feedback(models.Model):
    """Stores feedback submitted by users during logout."""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    enjoyed = models.TextField(
        "What did you enjoy most?",
        blank=True
    )
    improvements = models.TextField(
        "What could be improved?",
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """String representation of the feedback."""
        user_str = self.user.username if self.user else "Anonymous"
        date_str = self.created_at.strftime("%Y-%m-%d")
        return f"Feedback from {user_str} on {date_str}"