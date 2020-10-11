from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import *


def home_page(request):
    context = {
        "title": "Hello World",
        "content": "Learn Django",
    }
    if request.user.is_authenticated:
        context["premium_content"] = "Done"
    return render(request, 'homepage.html', context)


def about_page(request):
    context = {
        "title": "Hello about",
        "content": "Learn Django"
    }
    return render(request, 'homepage.html', context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Hello contact",
        "content": "Learn Django",
        "form": contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if request.method == "POST":
    #     print(request.POST)
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    return render(request, 'contact/view.html', context)


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    # print('User auth is', request.user.is_authenticated)
    # print()
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)
        # print('User auth is', request.user.is_authenticated)
        if user is not None:
            # print('User auth is', request.user.is_authenticated)
            login(request, user)
            # Redirect to a success page.
            context['form'] = LoginForm()
            return redirect("/")
        else:
            # Return an 'invalid login' error message
            print("Error login")
    return render(request, "auth/login.html", context)


User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)

        print(new_user)

        print(form.cleaned_data)
    return render(request, "auth/register.html", context)
