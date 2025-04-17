from django.urls import path, include
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.home, name='home'),
    path('hello/', views.hello_world, name='hello_world'),
    path('print/', views.print_hello, name='print_hello'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('load-template/', views.load_template, name='load_template'),
    
    # API endpoints
    path('api/contacts/', views.data, name='get_or_create_contacts'),  # GET and POST
    path('api/contacts/<int:pk>/', views.single_usr_data, name='single_user_operations'),  # GET, PUT, PATCH, DELETE
]