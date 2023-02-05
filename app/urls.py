from django.urls import path

from . import views

urlpatterns=[
    path("",views.index,name="base"),
    path("home/",views.home,name="home"),
    path("profile/",views.profile,name="home"),
]