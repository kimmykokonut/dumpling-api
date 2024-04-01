from rest_framework import serializers
from .models import Dumpling

class DumplingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Dumpling
    fields = ['id', 'name', 'description']