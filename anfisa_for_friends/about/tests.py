from django.test import TestCase
from django.urls import reverse


class AboutTest(TestCase):
    def test_description_status_code(self):
        response = self.client.get(reverse('about:description'))
        self.assertEqual(response.status_code, 200)

    def test_description_uses_correct_template(self):
        response = self.client.get(reverse('about:description'))
        self.assertTemplateUsed(response, 'about/description.html')
