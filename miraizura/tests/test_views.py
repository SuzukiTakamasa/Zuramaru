from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy

from ..models import Diary

class LoggedInTestCase(TestCase):
    """An unique TestCase class where the preparation processing that is common to each test class is overridden"""

    def setUp(self):
        """Previous settings before test methods are executed"""

        #Test user's password
        self.password = 'password'

        self.test_user = get_user_model().objects.create_user(
            username='test_user',
            email='test_user@example.com',
            password=self.password)

        self.client.login(email=self.test_user.email, password=self.password)

class TestDiaryCreateView(LoggedInTestCase):
    """Test class for DiaryCreateView"""

    def test_create_diary_success(self):

        #Post parameters
        params = {'title': 'test title',
                  'content': 'test content',
                  'photo1': '',
                  'photo2': '',
                  'photo3': ''}

        response = self.client.post(reverse_lazy('zuramaru:diary_create'), params)

        self.assertRedirects(response, reverse_lazy('zuramaru:diary_list'))

        self.assertEqual(Diary.objects.filter(title='test title').count(), 1)

    def test_create_diary_failure(self):

        response = self.client.post(revrse_lazy('zuramaru:diary_create'))

        self.assertFormError(response, 'form', 'title', 'This field is mandatory to fill out')

class TestDiaryUpdateView(LoggedInTestCase):
    """Test class for DiaryUpdateView"""

    def test_update_diary_success(self):

        diary = Diary.objects.create(user=self.test_user, title='title before update')

        #Post Parameters
        params = {'title': 'title after update'}

        response = self.client.post(reverse_lazy('zuramaru:diary_update', kwargs={'pk': diary.pk}), params)

        self.assertRedirects(response, reverse_lazy('zuramaru:zuramaru_detail', kwargs={'pk': diary.pk}))

        self.assertEqual(Diary.objects.get(pk=diary.pk).title, 'title after update')

    def test_update_diary_failure(self):

        response = self.client.post(reverse_lazy('zuramaru:diary_update', kwargs={pk: 999}))

        self.assertEqual(response.status_code, 404)

class TestDiaryDeleteView(LoggedInTestCase):
    """Test class for DiaryDeleteView"""

    def test_delete_diary_success(self):

        diary = Diary.objects.create(user=self.test_user, title='title')

        response = self.client.post(reverse_lazy('zuramaru:diary_delete', kwargs={'pk': diary.pk}))

        self.assertRedirects(response, reverse_lazy('zuramaru:diary_list'))

        self.assertEqual(Diary.objects.filter(pk=diary.pk).count(), 0)

    def test_delete_diary_failure(self):

        response = self.client.post(reverse_lazy('zuramaru:diary_delete', kwargs={'pk': 999}))

        self.assertEqual(response.status_code, 404)
        


