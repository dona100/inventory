from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Item

class ItemTests(APITestCase):
    def setUp(self):
        self.item = Item.objects.create(name="Test Item", description="Description", quantity=10, price=100)

    def test_create_item(self):
        data = {"name": "New Item", "description": "New Description", "quantity": 5, "price": 50}
        response = self.client.post(reverse('create_item'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_item(self):
        response = self.client.get(reverse('get_item', args=[self.item.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Test Item")

    def test_update_item(self):
        data = {"name": "Updated Item", "description": "Updated Description", "quantity": 15, "price": 150}
        response = self.client.put(reverse('update_item', args=[self.item.id]), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_item(self):
        response = self.client.delete(reverse('delete_item', args=[self.item.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
