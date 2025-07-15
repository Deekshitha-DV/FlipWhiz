from django.shortcuts import render

# Create your views here.
# In feedback/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import FeedbackForm

@login_required
def custom_logout_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            logout(request)
            # Set a session flag to trigger the animation
            request.session['just_logged_out'] = True
            return redirect('book_list')
    else:
        form = FeedbackForm()

    return render(request, 'registration/logout_feedback.html', {'form': form})