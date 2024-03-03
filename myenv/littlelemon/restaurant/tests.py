from django.test import TestCase
from .models import *

class MenuItemTest(TestCase):
  def test_get_item(self):
    item = Menu.objects.create(iD = 1000,title="IceCream", price=80, inventory=100)
    self.assertEqual(item.title, 'IceCream')
    self.assertEqual(item.price, 80)