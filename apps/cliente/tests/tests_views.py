from django.http import response
from django.test import TestCase

class ClienteTestCase(TestCase):
    def test_index_loads_properly(self):
        """The index page propely"""
        response = self.client.get('your_server_ip:8000')
        self.assertEqual(response.status_code, 404)