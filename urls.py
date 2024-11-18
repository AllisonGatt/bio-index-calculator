from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_sample/', views.add_sample, name='add_sample'),
    path('view_data/', views.view_data, name='view_data'),
    path('edit_sample/<int:sample_id>/', views.edit_sample, name='edit_sample'),  # Added URL for editing samples
    path('login/', views.login_view, name='login'),  # Handles user login
    path('logout/', views.logout_view, name='logout'),  # Handles user logout
    path('edit_sample/<int:sample_id>/', views.edit_sample, name='edit_sample'),  # Edit data
    path('delete_sample/<int:sample_id>/', views.delete_sample, name='delete_sample'),  # Delete data
    path('search/', views.search_data, name='search_data'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('edit_sample/<int:sample_id>/', views.edit_sample, name='edit_sample'),

]
