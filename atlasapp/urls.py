from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.loginpage,name="login"),
    path('register/',views.registerpage, name="register"),
    path('home/',views.home, name="home"),
    path('SupervisorHome/', views.SupervisorHome, name="SupervisorHome"),
    path('childhome/', views.childhome, name="childhome"),
    path('GannetHome/', views.GannetHome, name="GannetHome"),
    path('logout/',views.logout_view,name="logout"),
    path('manageMissions/',views.missions_view,name="manageMissions"),
    path(r'^delete/(?P<part_id>[0-9]+)/$', views.delete_mission, name='delete_mission'),
    path(r'^deleteitem/(?P<part_id>[0-9]+)/$', views.delete_item, name='delete_item'),
    path('sManageUsers/', views.sManageUsers, name="sManageUsers"),
    path(r'^deleteuser/(?P<part_id>[0-9]+)/$', views.delete_user, name='delete_user'),
    path(r'^(?P<id>\d+)/edit/$', views.edituser, name='edituser'),
    path(r'^(?P<id>\d+)/editItem/$', views.editItem, name='editItem'),
    path('gManageGames/', views.games_view, name='gManageGames'),
    path('sAddUser/', views.createUser, name="createUser"),
    path('bidudim/', views.bidudim, name="bidudim"),
    path('gManageUsers/', views.gManageUsers, name="gManageUsers"),
    path('gAddUser/', views.create_child, name="create_child"),
    path('addMissions/', views.createMission, name="createMission"),
    path('gAddItem/', views.createItem, name="createItem"),
    path(r'^deletechild/(?P<part_id>[0-9]+)/$', views.delete_child, name='delete_child'),
    path(r'^(?P<id>\d+)/editchild/$', views.edit_child, name='edit_child'),
    path('gManageMissions/',views.missions_view_gannet,name="gManageMissions"),
    path(r'^change_mission_status/(?P<part_id>[0-9]+)/$', views.get_mission_done, name='get_mission_done'),
    path('studycategory', views.studycategory, name='studycategory'),
    path('studysubcategory/<part_id>/', views.studysubcategory, name='studysubcategory'),
    path('studysubcategory/pick_game/<id>/', views.pickgame, name='pickgame'),
    path('game/', views.game, name='game')

]