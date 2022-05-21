from django.conf import settings
from django.urls import path

from . import views

urlpatterns=[
    path('', views.loginPage, name='loginPage'),
    path('home', views.home, name='home'),
    path('invalidLogin', views.invalidLogin, name='invalidLogin'),
    path('logout', views.logout, name='logout'),
]
