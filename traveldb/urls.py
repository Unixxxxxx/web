from django.urls import path
from .import views
urlpatterns = [
    path('',views.home, name='home'),
    path('contact',views.contact, name='contact'),
    path('About', views.About, name='About'),
    path('Services', views.Services, name='Services'),
    path('ne', views.ne, name='ne'),
    
]
