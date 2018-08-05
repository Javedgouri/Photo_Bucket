from . import views
from django.urls import path

urlpatterns = [
    path('', views.index_main),
    path('main',views.main, name='main'),
    path('index', views.index_main),
    path('goto', views.goto, name='goto'),
    path('uploadImage', views.uploadImage),
    path('getImage', views.getImage),
    path('logout', views.user_logout),
    path('sk', views.initialRequest),

]
