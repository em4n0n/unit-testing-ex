from django.test import TestCase
from models import MenuItem
from serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.serializer = MenuItemSerializer(instance=self.item)

    def test_get_item(self):
        self.assertEqual(self.serializer.data['title'], "IceCream")
        self.assertEqual(self.serializer.data['price'], "80.00")
        self.assertEqual(self.serializer.data['inventory'], 100)