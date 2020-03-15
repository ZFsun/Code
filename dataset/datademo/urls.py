from django.contrib import admin
from django.urls import path
from . import views

app_name = 'datademo'

urlpatterns = [
    path('index/', views.index.as_view(), name='index'),
]
