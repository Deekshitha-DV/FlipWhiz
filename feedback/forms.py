# In feedback/forms.py (new file)
from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['enjoyed', 'improvements']
        widgets = {
            'enjoyed': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Tell us what you liked...'}),
            'improvements': forms.Textarea(attrs={'rows': 4, 'placeholder': 'How can we make FlipWhiz better?'}),
        }