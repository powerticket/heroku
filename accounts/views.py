from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404, redirect, render

from .forms import MyUserCreationForm


# Create your views here.
def signup(request):
    if request.method == "POST":
        signup_form = MyUserCreationForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            auth_login(request, user)            
            return redirect('index')
    else:
        signup_form = MyUserCreationForm()
    context = {
        'signup_form': signup_form,
    }
    return render(request, 'accounts/signup.html', context)


def signout(request):
    pass


def login(request):
    if request.method == "POST":
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
            next_path = request.GET.get('next')
            if next_path:
                return redirect(next_path)            
            return redirect('index')
    else:
        login_form = AuthenticationForm()
    context = {
        'login_form': login_form,
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('index')


def profile(request, user_pk):
    User = get_user_model()
    user = get_object_or_404(User, pk=user_pk)
    context = {
        'user': user
    }
    return render(request, 'accounts/profile.html', context)
