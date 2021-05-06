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
        response = reverse('urlss : studycategory')
        self.assertEqual(response, '/urlss/studycategory')

    def test_studycategoryUrl_loading_notOk(self):
        response = reverse('urlss : studycategory')
        self.assertNotEqual(response, '/urlss/not_studycategory')
    # ------------------------------------------------------------------------------#