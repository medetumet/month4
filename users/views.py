from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from users.forms import LoginFrom

""" users/login.html """


# Create your views here.


def auth_view(request):
    if request.method == 'GET':
        context = {

        }
        return render(request, '')


def login_view(request):
    if request.method == "GET":
        context = {
            "form": LoginFrom
        }

        return render(request, "users/login.html", context=context)
