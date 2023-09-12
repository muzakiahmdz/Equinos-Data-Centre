from django.test import TestCase, Client
from .models import Character, Item

class MainTest(TestCase):
    
    # def test_character_list_url_exists(self):
    #     response = Client().get('/characters/')  # Sesuaikan dengan URL karakter Anda
    #     self.assertEqual(response.status_code, 200)

    # def test_item_list_url_exists(self):
    #     response = Client().get('/items/')  # Sesuaikan dengan URL item 
    #     self.assertEqual(response.status_code, 200)

    # def test_character_list_uses_template(self):
    #     response = Client().get('/characters/')  # Sesuaikan dengan URL karakter 
    #     self.assertTemplateUsed(response, 'character_list.html')  # Sesuaikan dengan template karakter

    # def test_item_list_uses_template(self):
    #     response = Client().get('/items/')  # Sesuaikan dengan URL item
    #     self.assertTemplateUsed(response, 'item_list.html')  # Sesuaikan dengan template item

    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')


