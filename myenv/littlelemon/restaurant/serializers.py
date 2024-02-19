from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class MenuItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = Menu
    fields = ['iD', 'title', 'price', 'inventory']

class BookingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Booking