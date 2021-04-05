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
    path('sManageUsers/', views.sManageUsers, name="sManageUsers"),
    path(r'^deleteuser/(?P<part_id>[0-9]+)/$', views.delete_user, name='delete_user'),
    path(r'^(?P<id>\d+)/edit/$', views.edituser, name='edituser'),
    path('sAddUser/', views.createUser, name="createUser"),
    path('bidudim/', views.bidudim, name="bidudim"),
    path('gManageUsers/', views.gManageUsers, name="gManageUsers"),
    path('gAddUser/', views.create_child, name="create_child"),
    path('addMissions/', views.createMission, name="createMission")

]