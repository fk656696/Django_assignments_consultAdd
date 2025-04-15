from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.hello_world, name='hello'),
    
    path('admin/', admin.site.urls),
    path('', include('Loginify.urls')),

    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('', views.signup), 
    ]