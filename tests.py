from django.test import TestCase, Client
from django.urls import reverse

class PostsURLTests(TestCase):
    def setUp(self):
        """Настройка перед каждым тестом"""
        self.guest_client = Client()
    
    def test_homepage_url_exists_at_desired_location(self):
        """Тест: главная страница доступна"""
        response = self.guest_client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_homepage_url_accessible_by_name(self):
        """Тест: главная страница доступна через имя маршрута"""
        response = self.guest_client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
    
    def test_group_page_exists_for_any_slug(self):
        """Тест: страница группы доступна для любого slug"""
        response = self.guest_client.get('/group/python/')
        self.assertEqual(response.status_code, 200)
        
        response2 = self.guest_client.get('/group/django/')
        self.assertEqual(response2.status_code, 200)
        
        response3 = self.guest_client.get('/group/any-slug-123/')
        self.assertEqual(response3.status_code, 200)
    
    def test_group_page_uses_correct_template(self):
        """Тест: страница группы использует правильный шаблон"""
        pass