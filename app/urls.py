from django.urls import path

from . import views

urlpatterns=[
    path("",views.base,name="base"),
    path("home/",views.home,name="home"),
    path("profile/",views.profile,name="home"),
    path("champions/",views.champions,name="champions"),
    path("live/",views.live,name="live"),
    path("tierlist/",views.tierlist,name="tierlist"),
]