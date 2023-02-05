from django.shortcuts import render
from django.http import HttpResponse


def index(response):
    return render(response, "app/base.html", {})


def home(response):
    return render(response, "app/home.html", {})

def profile(response):
    return render(response, "app/profile.html", {})

