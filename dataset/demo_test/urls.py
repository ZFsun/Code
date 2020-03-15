from django.urls import path, include
from . import views

app_name = 'demo_test'

urlpatterns = [
    path(r'demo_test/', views.index, name='index'),
    path(r'bar/', views.ChartView.as_view(), name='demo'),
    path(r'test2_index/', views.IndexView.as_view(), name='demo'),
]

