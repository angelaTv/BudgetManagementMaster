"""accounts URL Configuration

"""
from django.shortcuts import render
from django.urls import path, include
from accounts import views

urlpatterns = [
    path('register/', views.CreateUser.as_view(), name='register'),
    path('register/login/', views.LoginView.as_view(), name="login"),
    path('register/login/home/', lambda request: render(request, "accounts/home.html"), name='home'),
    path('', views.Logout.as_view(), name="logout"),
    path('myprofile', views.Userprofile.as_view(), name="profile"),
]
