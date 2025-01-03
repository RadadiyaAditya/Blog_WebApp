from django.urls import path
from . import views

urlpatterns = [
    #blog-home is the name given to the route
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]