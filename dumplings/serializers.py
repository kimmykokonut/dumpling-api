from rest_framework import serializers
from .models import Dumpling, Tag, Origin

class DumplingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Dumpling
    fields = ['id', 'name', 'description', 'origin']

class TagSerializer(serializers.ModelSerializer):
  # need to make dumplings in json body optional
  dumplings = serializers.PrimaryKeyRelatedField(many=True, queryset=Dumpling.objects.all(), required=False)
  class Meta:
    model = Tag
    fields = ['id', 'name', 'dumplings']
    # 'dumplings' is M:M FK

class OriginSerializer(serializers.ModelSerializer):
  class Meta:
    model = Origin
    fields = ['id', 'country']