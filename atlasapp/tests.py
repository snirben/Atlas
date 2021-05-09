from django.test import TestCase
from django.test import Client
from .models import *
from django.urls import reverse

class UserTestCreate(TestCase):

    def setUp(self):
        self.gannet = User.objects.get_or_create(
            username='test_gannet_username',
            password='test_gannet_password',
            name='test_gannet_name',
            lastname='test_gannet_lastname',
            email='test_gannet_email',
            phone='test_gannet_phone',
            mevodad=False,
            covid=False,
            role=1)

        self.child = User.objects.get_or_create(
            username='test_child_username',
            password='test_child_password',
            name='test_child_name',
            lastname='test_child_lastname',
            email='test_child_email',
            phone='test_child_phone',
            mevodad=False,
            covid=True,
            role=2)
        self.gannet[0].save()
        self.child[0].save()

    def test_check_gannet_is_created(self):
        gannet = User.objects.get(username="test_gannet_username")
        self.assertEqual(gannet.username, "test_gannet_username")

    def test_check_child_is_created(self):
        child = User.objects.get(username="test_child_username")
        self.assertEqual(child.username, "test_child_username")

class UserTestViews(TestCase):

    def test_index_loads_properly(self):
        c = Client()
        response = c.post('', {'username': 'admin', 'password': '123456'})
        response.status_code

        self.assertEqual(response.status_code, 200)

    def test_login_loads_properly(self):
        response = self.client.get('http://127.0.0.1:8000')
        self.assertEqual(response.status_code, 200)

    def test_404_loads_properly(self):
        response = self.client.get('http://127.0.0'
                                   '.1:8000/nonepage')
        self.assertEqual(response.status_code, 404)

class SubjectTestCreate(TestCase):

    def setUp(self):
        self.subject = Subject.objects.get_or_create(
            name='test_subject_name',
            image='test_subject_image',
            audio='test_subject_audio',
        )
        self.subject[0].save()

    def test_check_subject_is_created(self):
        subject = Subject.objects.get(name="test_subject_name")
        self.assertEqual(subject.name, "test_subject_name")

class SubSubjectTestCreate(TestCase):

    def setUp(self):
        self.subSubject = SubSubject.objects.get_or_create(
            name='test_subSubject_name',
            subject='test_subSubject_subject',
            gametype='test_subSubject_gametype',
            image='test_subSubject_image',
            audio='test_subSubject_audio',
        )
        self.subSubject[0].save()

    def test_check_subSubject_is_created(self):
        subSubject = SubSubject.objects.get(name="test_subSubject_name")
        self.assertEqual(subSubject.name, "test_subSubject_name")

class ItemTestCreate(TestCase):

    def setUp(self):
        self.item = Item.objects.get_or_create(
            subject='test_item_subject',
            color='test_item_color',
            gametype='test_item_gametype',
            image='test_item_image',
            audio='test_item_audio',
        )
        self.Item[0].save()

    def test_check_Item_is_created(self):
         item = Item.objects.get(subject ="test_item_subject")
         self.assertEqual(item.subject, "test_item_subject")


class GameTestCreate(TestCase):

    def setUp(self):
        self.game = Game.objects.get_or_create(
            user ='test_game_user',
            created_at='test_game_created_at',
            steps='test_game_steps',
        )
        self.game[0].save()

    def test_check_Game_is_created(self):
        game = Game.objects.get(name="test_game_user")
        self.assertEqual(game.user, "test_game_user")

class testUrl(TestCase):
    def setUp(self):
        self.urlsTest = User.objects.get_or_create(
            nameProject='testProjectName',
            content='test_userStoryTest_content',
            priority='test_userStoryTest_priority',
            assign='test_teammate_userName',
            status='Not Done'
        )
        self.urlsTest[0].save()

    # ------------------------------------------------------------------------------#
    def test_studycategoryUrl_loading_ok(self):
        response = reverse('studycategory')
        self.assertEqual(response, '/studycategory')

    def test_studycategoryUrl_loading_notOk(self):
        response = reverse('studycategory')
        self.assertNotEqual(response, '/not_studycategory')
    # ------------------------------------------------------------------------------#

    # ------------------------------------------------------------------------------#
    def test_studySubcategoryUrl_loading_ok(self):
        response = reverse('studysubcategory', kwargs={'id': '0'})
        self.assertEqual(response, '/studysubcategory/0/')

    def test_studySubcategoryUrl_loading_notOk(self):
        response = reverse('studysubcategory')
        self.assertNotEqual(response, '/studysubcategory/1/')
    # ------------------------------------------------------------------------------#

    # ------------------------------------------------------------------------------#
    def test_studySubcategoryPickGameUrl_loading_ok(self):
        response = reverse('studysubcategoryPickGame', kwargs={'id': '0'})
        self.assertEqual(response, '/studysubcategory/pick_game/0/')

    def test_studySubcategoryPickGameUrl_loading_notOk(self):
        response = reverse('studysubcategoryPickGame', kwargs={'id': '0'})
        self.assertNotEqual(response, '/studysubcategory/pick_game/1/')
    # ------------------------------------------------------------------------------#

    # ------------------------------------------------------------------------------#
    def test_memoryGameUrl_loading_ok(self):
        response = reverse('memoryGame', kwargs={'id': '0'})
        self.assertEqual(response, 'appname/memory_game/0/')

    def test_memoryGameUrl_loading_notOk(self):
        response = reverse('memoryGame', kwargs={'id': '0'})
        self.assertNotEqual(response, 'appname/memory_game/1/')
    # ------------------------------------------------------------------------------#

    # ------------------------------------------------------------------------------#
    def test_someInThePictureView_loading_ok(self):
        response = reverse('someInThePictureView', kwargs={'id': '0'})
        self.assertEqual(response, 'appname/someInThePicture/0/')

    def test_someInThePictureView_loading_notOk(self):
        response = reverse('someInThePictureView', kwargs={'id': '0'})
        self.assertNotEqual(response, 'appname/someInThePicture/1/')
    # ------------------------------------------------------------------------------#

    # ------------------------------------------------------------------------------#
    def test_someInThePictureView_loading_ok(self):
        response = reverse('someInThePictureView', kwargs={'id': '0'})
        self.assertEqual(response, 'appname/someInThePicture/0/')

    def test_someInThePictureView_loading_notOk(self):
        response = reverse('someInThePictureView', kwargs={'id': '0'})
        self.assertNotEqual(response, 'appname/someInThePicture/1/')
    # ------------------------------------------------------------------------------#

    # ------------------------------------------------------------------------------#
    def test_colorGame_loading_ok(self):
        response = reverse('colorGame', kwargs={'id': '0'})
        self.assertEqual(response, 'appname/colorgame/0/')

    def test_colorGame_loading_notOk(self):
        response = reverse('colorGame', kwargs={'id': '0'})
        self.assertNotEqual(response, 'appname/colorgame/1/')
    # ------------------------------------------------------------------------------#

    # ------------------------------------------------------------------------------#
    def test_login_loading_ok(self):
        response = reverse('login')
        self.assertEqual(response, 'appname/')

    def test_login_loading_notOk(self):
        response = reverse('login')
        self.assertNotEqual(response, 'appname/not')
    # ------------------------------------------------------------------------------#

    # ------------------------------------------------------------------------------#
    def test_register_loading_ok(self):
        response = reverse('register')
        self.assertEqual(response, 'appname/register')

    def test_register_loading_notOk(self):
        response = reverse('login')
        self.assertNotEqual(response, 'appname/not_register')
    # ------------------------------------------------------------------------------#

    # ------------------------------------------------------------------------------#
    def test_home_loading_ok(self):
        response = reverse('home')
        self.assertEqual(response, 'appname/home')

    def test_home_loading_notOk(self):
        response = reverse('home')
        self.assertNotEqual(response, 'appname/not_home')
    # ------------------------------------------------------------------------------#

    # ------------------------------------------------------------------------------#
    def test_SupervisorHome_loading_ok(self):
        response = reverse('SupervisorHome')
        self.assertEqual(response, 'appname/SupervisorHome')

    def test_SupervisorHome_loading_notOk(self):
        response = reverse('SupervisorHome')
        self.assertNotEqual(response, 'appname/not_SupervisorHome')
    # ------------------------------------------------------------------------------#

    # ------------------------------------------------------------------------------#
    def test_childHome_loading_ok(self):
        response = reverse('childHome')
        self.assertEqual(response, 'appname/childHome')

    def test_childHome_loading_notOk(self):
        response = reverse('childHome')
        self.assertNotEqual(response, 'appname/not_childHome')
    # ------------------------------------------------------------------------------#

    # ------------------------------------------------------------------------------#
    def test_GannetHome_loading_ok(self):
        response = reverse('GannetHome')
        self.assertEqual(response, 'appname/GannetHome')

    def test_GannetHome_loading_notOk(self):
        response = reverse('GannetHome')
        self.assertNotEqual(response, 'appname/not_GannetHome')
    # ------------------------------------------------------------------------------#

    # ------------------------------------------------------------------------------#
    def test_logout_loading_ok(self):
        response = reverse('logout')
        self.assertEqual(response, 'appname/logout')

    def test_logout_loading_notOk(self):
        response = reverse('logout')
        self.assertNotEqual(response, 'appname/not_logout')
    # ------------------------------------------------------------------------------#

    # ------------------------------------------------------------------------------#
    def test_manageMissions_loading_ok(self):
        response = reverse('manageMissions')
        self.assertEqual(response, 'appname/manageMissions')

    def test_manageMissions_loading_notOk(self):
        response = reverse('manageMissions')
        self.assertNotEqual(response, 'appname/not_manageMissions')
    # ------------------------------------------------------------------------------#

    # ------------------------------------------------------------------------------#
    def test_sManageUsers_loading_ok(self):
        response = reverse('sManageUsers')
        self.assertEqual(response, 'appname/sManageUsers')

    def test_sManageUsers_loading_notOk(self):
        response = reverse('sManageUsers')
        self.assertNotEqual(response, 'appname/not_sManageUsers')
    # ------------------------------------------------------------------------------#

    # ------------------------------------------------------------------------------#
    def test_sManageUsers_loading_ok(self):
        response = reverse('sManageUsers')
        self.assertEqual(response, '/sManageUsers')

    def test_sManageUsers_loading_notOk(self):
        response = reverse('sManageUsers')
        self.assertNotEqual(response, '/not_sManageUsers')
    # ------------------------------------------------------------------------------#

    def test_save_color_game_loading_ok(self):
        response = reverse('save-colorgame-result')
        self.assertEqual(response, '/ajax/save-colorgame-result')

    def test_save_color_game_loading_notOk(self):
        response = reverse('save-colorgame-result')
        self.assertNotEqual(response, '/ajax/not_save-colorgame-result')

    # ------------------------------------------------------------------------------#

    def test_save_game_result_loading_ok(self):
        response = reverse('save-game-result')
        self.assertEqual(response, '/ajax/save-game-result')

    def test_save_game_result_loading_notOk(self):
        response = reverse('save-game-result')
        self.assertNotEqual(response, '/ajax/not_save-game-result')

    # ------------------------------------------------------------------------------#

    def test_someInThePictureGame_loading_ok(self):
        response = reverse('someInThePictureGame', kwargs={'id': '0'})
        self.assertEqual(response, '/someInThePictureGame/0/')

    def test_someInThePictureGame_loading_notOk(self):
        response = reverse('someInThePictureGame', kwargs={'id': '0'})
        self.assertNotEqual(response, '/someInThePictureGame/1/')

    # ------------------------------------------------------------------------------#

    def test_save_someinthepicture_result_loading_ok(self):
        response = reverse('save-someinthepicture-result')
        self.assertEqual(response, '/ajax/save-someinthepicture-result')

    def test_save_someinthepicture_result_loading_notOk(self):
        response = reverse('save-someinthepicture-result')
        self.assertNotEqual(response, '/ajax/not_save-someinthepicture-result')

    # ------------------------------------------------------------------------------#

    def test_gManageMissions_loading_ok(self):
        response = reverse('gManageMissions')
        self.assertEqual(response, '/gManageMissions')

    def test_gManageMissions_loading_notOk(self):
        response = reverse('gManageMissions')
        self.assertNotEqual(response, '/not_gManageMissions')

    # ------------------------------------------------------------------------------#

    def test_gAddItem_loading_ok(self):
        response = reverse('gAddItem')
        self.assertEqual(response, '/gAddItem')

    def test_gAddItem_loading_notOk(self):
        response = reverse('gAddItem')
        self.assertNotEqual(response, '/not_gAddItem')

    # ------------------------------------------------------------------------------#

    def test_addMissions_loading_ok(self):
        response = reverse('addMissions')
        self.assertEqual(response, '/addMissions')

    def test_addMissions_loading_notOk(self):
        response = reverse('addMissions')
        self.assertNotEqual(response, '/not_addMissions')

    # ------------------------------------------------------------------------------#

    def test_gAddUser_loading_ok(self):
        response = reverse('gAddUser')
        self.assertEqual(response, '/gAddUser')

    def test_gAddUser_loading_notOk(self):
        response = reverse('gAddUser')
        self.assertNotEqual(response, '/not_gAddUser')

    # ------------------------------------------------------------------------------#

    def test_gManageUsers_loading_ok(self):
        response = reverse('gManageUsers')
        self.assertEqual(response, '/gManageUsers')

    def test_gManageUsers_loading_notOk(self):
        response = reverse('gManageUsers')
        self.assertNotEqual(response, '/not_gManageUsers')

    # ------------------------------------------------------------------------------#

    def test_bidudim_loading_ok(self):
        response = reverse('bidudim')
        self.assertEqual(response, '/bidudim')

    def test_bidudim_loading_notOk(self):
        response = reverse('bidudim')
        self.assertNotEqual(response, '/not_bidudim')

    # ------------------------------------------------------------------------------#

    def test_sAddUser_loading_ok(self):
        response = reverse('sAddUser')
        self.assertEqual(response, '/sAddUser')

    def test_sAddUser_loading_notOk(self):
        response = reverse('sAddUser')
        self.assertNotEqual(response, '/not_sAddUser')

    # ------------------------------------------------------------------------------#

    def test_gManageGames_loading_ok(self):
        response = reverse('gManageGames')
        self.assertEqual(response, '/gManageGames')

    def test_gManageGames_loading_notOk(self):
        response = reverse('gManageGames')
        self.assertNotEqual(response, '/not_gManageGames')