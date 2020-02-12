from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from dota_analytics.forms import PasswordResetForm
from dota_analytics.forms import SignUpForm
# Create your views here.

@login_required(login_url="/login/")
def home(request):
    return render(request, 'dota_analytics/index.html')

def prediction(request):
    return render(request, 'dota_analytics/Queue.html')

def password_reset(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
    else:
        form = PasswordResetForm()
    return render(request, 'registration/password_reset_form.html', {'form': form})


def password_reset_done(request):
    return render(request, 'registration/password_reset_done.html')


def password_reset_confirm(request):
    return render(request, 'registration/password_reset_confirm.html')


def password_reset_complete(request):
    return render(request, 'registration/password_reset_complete.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'registration/login.html')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
