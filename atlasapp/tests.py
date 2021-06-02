from django.test import TestCase
from django.test import Client
from .models import *
from django.urls import reverse
from django.contrib.staticfiles import finders
from django.contrib.staticfiles.storage import staticfiles_storage
import requests


class DbTestCase(TestCase):

    def dbconnection(self):
        from django.db import connections
        from django.db.utils import OperationalError
        db_conn = connections['default']
        try:
            c = db_conn.cursor()
        except OperationalError:
            connected = False
        else:
            connected = True
        self.assertEqual(connected, True)


class StaticTestCase(TestCase):
    # check if we have valid access to all of the static files
    def staticfiles(self):
        absolute_path = finders.find('js/game.js')
        assert staticfiles_storage.exists(absolute_path)


class CheckInternetConnection(TestCase):
    # we want to check that we can pull all cdn and we have interntes
    def interneton(self):
        # google check
        url = "8.8.8.8"
        timeout = 5
        answer = ''
        try:
            request = requests.get(url, timeout=timeout)
            answer = "Connected to the Internet"
            self.assertEqual(answer, "Connected to the Internet")
        except (requests.ConnectionError, requests.Timeout) as exception:
            answer = "No internet connection."
            self.assertEqual(answer, "Connected to the Internet")


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
        self.child = User.objects.create_user(
            username='admin',
            password='123456',
            name='test_child_name',
            lastname='test_child_lastname',
            email='test_child_email',
            phone='test_child_phone',
            mevodad=False,
            covid=True,
            role=2)
        c = Client()
        response = c.post('', {'username': 'admin', 'password': '123456'})

        self.assertEqual(response.status_code, 302)

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
            image='',
            audio='',
        )
        self.subject[0].save()

    def test_check_subject_is_created(self):
        subject = Subject.objects.get(name="test_subject_name")
        self.assertEqual(subject.name, "test_subject_name")


class SubSubjectTestCreate(TestCase):

    def setUp(self):
        subject = Subject.objects.get_or_create(
            name='test_subject_name',
            image='',
            audio='',
        )
        self.subSubject = SubSubject.objects.get_or_create(
            name='test_subSubject_name',
            subject=Subject.objects.get(pk=1),
            gametype='test_subSubject_gametype',
            image='',
            audio='',
        )
        self.subSubject[0].save()

    def test_check_subSubject_is_created(self):
        subSubject = SubSubject.objects.get(name="test_subSubject_name")
        self.assertEqual(subSubject.name, "test_subSubject_name")

class ItemTestCreate(TestCase):

    def setUp(self):
        subject = Subject.objects.get_or_create(
            name='test_subject_name',
            image='',
            audio='',
        )
        subSubject = SubSubject.objects.get_or_create(
            name='test_subSubject_name',
            subject=Subject.objects.get(pk=1),
            gametype='test_subSubject_gametype',
            image='',
            audio='',
        )
        self.item = Item.objects.get_or_create(
            subject=SubSubject.objects.get(pk=1),
            color='green',
            gametype='memory',
            image='',
            audio='',
        )


    def test_check_Item_is_created(self):
         item = Item.objects.get(pk =1)
         self.assertEqual(item.id, 1)


class GameTestCreate(TestCase):

    def setUp(self):
        child = User.objects.get_or_create(
            username='test_game_user',
            password='test_child_password',
            name='test_child_name',
            lastname='test_child_lastname',
            email='test_child_email',
            phone='test_child_phone',
            mevodad=False,
            covid=True,
            role=2)

        self.game = Game.objects.get_or_create(
            user =User.objects.get(pk=1),
            created_at='2021-02-20 18:00',
            steps=30,
        )
        self.game[0].save()

    def test_check_Game_is_created(self):
        child = User.objects.get(username="test_game_user")
        game = Game.objects.get(pk=child.id)
        self.assertEqual(game.user.username, "test_game_user")

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

class UserTestStory4(TestCase):
    def test_page_loads_properly(self):
        self.supervisor = User.objects.create_user(
            username='supervisor',
            password='123456',
            name='test_supervisor_name',
            lastname='test_supervisor_lastname',
            email='test_supervisor_email',
            phone='test_supervisor_phone',
            mevodad=False,
            covid=True,
            role=0)
        c = Client()
        response = c.post('', {'username': 'supervisor', 'password': '123456'})
        response = self.client.get('http://127.0.0.1:8000/SupervisorHome')
        self.assertEqual(response.status_code, 301)  # because of redirect


class UserTestStory5(TestCase):
    def test_page_loads_properly(self):
        self.supervisor = User.objects.create_user(
            username='supervisor',
            password='123456',
            name='test_supervisor_name',
            lastname='test_supervisor_lastname',
            email='test_supervisor_email',
            phone='test_supervisor_phone',
            mevodad=False,
            covid=True,
            role=0)
        c = Client()
        response = c.post('', {'username': 'supervisor', 'password': '123456'})
        response = self.client.get('http://127.0.0.1:8000/SupervisorHome')
        self.assertEqual(response.status_code, 301)  # because of redirect

#integration
class UserTestStory21(TestCase):
    def test_contact_created_loads_properly(self):
        self.user = User.objects.create_user(
            username='kidgarden',
            password='123456',
            name='test_kidgarden_name',
            lastname='test_kidgarden_lastname',
            email='test_kidgarden_email',
            phone='test_kidgarden_phone',
            mevodad=False,
            covid=True,
            role=2)
        self.star = Star.objects.create(user=self.user)
        self.assertEqual(self.star.id, 1)

    def test_contact_deleted_loads_properly(self):
        self.user = User.objects.create_user(
            username='kidgarden',
            password='123456',
            name='test_kidgarden_name',
            lastname='test_kidgarden_lastname',
            email='test_kidgarden_email',
            phone='test_kidgarden_phone',
            mevodad=False,
            covid=True,
            role=2)
        self.star = Star.objects.create(user=self.user)
        starid = self.star.id
        self.star.delete()
        star_exist = Star.objects.filter(pk=starid)
        self.assertEqual(len(star_exist), 0)