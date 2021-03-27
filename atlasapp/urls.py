from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.loginpage,name="login"),
    path('register/',views.registerpage, name="register"),
    path('home/',views.home, name="home"),
    path('logout/',views.logout_view,name="logout")
]