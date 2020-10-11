from django.http import HttpResponse
from django.shortcuts import render

from .forms import *

def home_page(request):
    context = {
        "title": "Hello World",
        "content": "Learn Django"
    }
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
    print('User auth is', request.user.is_authenticated)
    # print()
    if form.is_valid():
        print(form.cleaned_data)
        context['form'] = LoginForm
        ()
    return render(request, "auth/login.html" , context)

def register_page(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, "auth/register.html" , {})

