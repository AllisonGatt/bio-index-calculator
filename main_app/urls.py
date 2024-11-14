# main_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_sample/', views.add_sample, name='add_sample'),
    path('view_data/', views.view_data, name='view_data'),
]
