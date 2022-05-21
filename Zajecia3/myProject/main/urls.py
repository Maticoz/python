from django.conf import settings
from django.urls import path

from . import views

urlpatterns=[
    path('', views.login, name='login'),
    path('home', views.home, name='home'),
    path('logout', views.logout, name='logout'),
    path('error', views.error, name='error'),
]
