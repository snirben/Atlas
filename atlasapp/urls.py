from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.loginpage,name="login"),
    path('register/',views.registerpage, name="register"),
    path('home/',views.home, name="home"),
    path('logout/',views.logout_view,name="logout"),
    path('manageMissions/',views.missions_view,name="manageMissions"),
    path(r'^delete/(?P<part_id>[0-9]+)/$', views.delete_mission, name='delete_mission'),
    path('addMissions/', views.createMission, name="createMission")
]