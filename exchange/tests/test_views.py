from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
from exchange import service


class IndexPageTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_view_GET(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'exchange/index.html')

    def test_view_POST(self):
        currencies = service.current_exchanges()
        post_data = {
            'from-curr': 'USD',
            'to-curr': 'RUB',
            'from-amount': 100,
        }
        response = self.client.post(reverse('index'), post_data)
        result = round(
            currencies['RUB'] / currencies['USD'] * 100, 2
        )
        self.assertEqual(response, result)



