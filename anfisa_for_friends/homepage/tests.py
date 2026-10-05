from django.test import TestCase
from django.urls import reverse


class HomepageTest(TestCase):
    def test_index_status_code(self):
        response = self.client.get(reverse('homepage:index'))
        self.assertEqual(response.status_code, 200)

    def test_index_uses_correct_template(self):
        response = self.client.get(reverse('homepage:index'))
        self.assertTemplateUsed(response, 'homepage/index.html')
