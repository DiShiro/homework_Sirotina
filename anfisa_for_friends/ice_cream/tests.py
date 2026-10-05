from django.test import TestCase
from django.urls import reverse


class IceCreamTest(TestCase):
    def test_list_status_code(self):
        response = self.client.get(reverse('ice_cream:ice_cream_list'))
        self.assertEqual(response.status_code, 200)

    def test_list_uses_correct_template(self):
        response = self.client.get(reverse('ice_cream:ice_cream_list'))
        self.assertTemplateUsed(response, 'ice_cream/list.html')

    def test_list_context_has_catalog(self):
        response = self.client.get(reverse('ice_cream:ice_cream_list'))
        self.assertIn('ice_cream_list', response.context)
        self.assertEqual(len(response.context['ice_cream_list']), 3)

    def test_detail_status_code(self):
        response = self.client.get(
            reverse('ice_cream:ice_cream_detail', args=[0])
        )
        self.assertEqual(response.status_code, 200)

    def test_detail_uses_correct_template(self):
        response = self.client.get(
            reverse('ice_cream:ice_cream_detail', args=[0])
        )
        self.assertTemplateUsed(response, 'ice_cream/detail.html')

    def test_detail_context(self):
        response = self.client.get(
            reverse('ice_cream:ice_cream_detail', args=[0])
        )
        self.assertEqual(response.context['ice_cream']['id'], 0)
