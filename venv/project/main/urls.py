from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="base"),
    path("about/", views.about, name="about"),
    path("setting/", views.setting, name="setting"),
    path("login/", views.login, name="about"),
    path("logout/", views.logout, name="setting"),
     path("registration/", views.register, name="setting"),
]