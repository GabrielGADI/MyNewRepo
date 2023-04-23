from django.test import TestCase

# Create your tests here.

from .models import Client

class ClientTestCase(TestCase):
    def setUp(self):
        self.client = Client.objects.create(
            first_name='John',
            last_name='Doe',
            email='johndoe@example.com',
            phone='1234567890',
            address='123 Main St, Anytown USA'
        )

    def test_client_created(self):
        client = Client.objects.get(first_name='John')
        self.assertEqual(client.last_name, 'Doe')
        self.assertEqual(client.email, 'johndoe@example.com')
        self.assertEqual(client.phone, '1234567890')
        self.assertEqual(client.address, '123 Main St, Anytown USA')