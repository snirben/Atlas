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
    path('memory_game/<subsubject_id>/', views.memory_game, name='memory_game'),
    path('someInThePicture/<subject_id>/', views.someInThePicture_view, name='someInThePicture'),
    path('someInThePictureGame/<subject_id>/', views.someInThePictureGame, name='someInThePictureGame'),
    path('colorgame/<subsubject_id>/', views.colorgame, name='colorgame'),
    path('someInThePictureGame/<subject_id>/', views.someInThePictureGame, name='someInThePictureGame'),
    path('ajax/save-someinthepicture-result/', views.endsomeinthepicturegame, name='endsomeinthepicturegame'),
    path('someInThePictureGame/<subject_id>/', views.someInThePictureGame, name='someInThePictureGame'),
    path('ajax/save-game-result/', views.end_memory_game, name='save-game-result'),
    path('ajax/save-colorgame-result/', views.end_color_game, name='save-colorgame-result'),
    path('sComplainpage/', views.sComplainpage_view, name="sComplainpage"),
    path('update-complain/<part_id>', views.update_complain, name="update_complain"),
    path('addcomplain/', views.createcomplain, name="createcomplain"),
    path('reports/', views.reports, name="reports"),
    path('messages/', views.messages2, name="messages"),
    path('add_messages/', views.add_messages, name="add_messages"),
    path('create_capsules/', views.capsules_view, name="capsules_view"),
    path('gBidudim/', views.gBidudim, name="gBidudim"),
    path('contact_page/', views.contact_page, name="contact_page"),
    path('send_emails/', views.send_emails, name="send_emails"),
    path('messages_to_parents/', views.messages_to_parents, name="messages_to_parents"),
    path('g_add_complain/', views.gannet_create_complain, name="gannet_create_complain"),
    path('stars',views.star_page,name="star_page"),
    path('ajax/create-star/', views.pick_star, name='create-star'),
    path('health/', views.health, name='health'),
    path('editmyhealth/<id>', views.myhealthedit, name='ceditchild'),
    path('myhealth/<user_id>', views.myhealth, name='myhealth'),
    path('mymessages/', views.mymessages, name='mymessages')



]