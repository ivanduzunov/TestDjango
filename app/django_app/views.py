from django.shortcuts import render, redirect
import os
import sys
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm, ProfileForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from bs4 import BeautifulSoup


def get_errors_from_forms(form_str):
    soup = BeautifulSoup(form_str, 'html.parser')
    return '\n'.join([el.text for el in soup.find_all('ul', {'class': 'errorlist'})])

#
def register_view(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        # profile_form = ProfileForm()
        mess = get_errors_from_forms(str(user_form))
        if user_form.is_valid():
            user = user_form.save()
            user.refresh_from_db()
            user.save()
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect("/", {'message': 'Account created!'})
        return render(request, "register.html", {'form': user_form, 'message': mess})
    form = SignUpForm()
    return render(request, "register.html", {'form': form})

def login_view(request):
    mess = ''
    form = AuthenticationForm()
    if not request.method == 'POST': return render(request, "login.html", {'message': mess, 'form': form})
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
        mess = 'Logged in successfully!'
        user = form.get_user()
        login(request, user)
        return redirect('/', {'message': mess, 'user': user.username})
    mess = 'Invalid username or password!'
    return render(request, "login.html", {'message': mess, 'form': 'form'})


@login_required(login_url="/login")
def logout_view(request, *args, **kwargs):
    logout(request)
    return redirect("/login")


@login_required(login_url='/login/')
def home_view(request):
    directory_path = os.getcwd()
    return render(request, "home.html")

