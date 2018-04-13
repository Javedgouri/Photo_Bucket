from . import views
from django.urls import path

urlpatterns = [
    path('home', views.index),
    path('main',views.main),
]
