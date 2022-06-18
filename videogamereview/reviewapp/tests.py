from django.test import TestCase
from .models import Videogame, Vgreview
from django.urls import reverse_lazy, reverse

# Create your tests here.
class VideoGameTest(TestCase):
    def setUp(self):
        self.type=Videogame(Title='test title')

    def test_videogamegstring(self):
        self.assertEqual(str(self.type), 'test title')

    def test_tablename(self):
        self.assertEqual(str(Videogame._meta.db_table), 'videogame')

class VgreviewTest(TestCase):
    def setUp(self):
        self.type=Vgreview(Title='review 1')

    def test_vgreviewstring(self):
        self.assertEqual(str(self.type), 'review 1')

    def test_tablename(self):
        self.assertEqual(str(Vgreview._meta.db_table), 'vgreview')

class New_Videogame_Authentication_Test(TestCase):
    def setup(self):
        self.test_user=User.objects.create_user(username='testuser1', password='P@ssw0rd1')
        self.Videogame=Videogame.objects.create(Title='title 1')
    
    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('addvideogame'))
        self.assertRedirects(response, '/accounts/login/?next=/reviewapp/addvideogame/')

class New_Vgreview_Authentication_Test(TestCase):
    def setup(self):
        self.test_user=User.objects.create_user(username='testuser1', password='P@ssw0rd1')
        self.Vgreview=Vgreview.objects.create(Title='title 1')
    
    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('addreview'))
        self.assertRedirects(response, '/accounts/login/?next=/reviewapp/addreview/')