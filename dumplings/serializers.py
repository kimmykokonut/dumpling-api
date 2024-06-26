from rest_framework import serializers
#from rest_framework.validators import UniqueValidator
from .models import Dumpling, Tag, Origin
from django.contrib.auth.models import User

class OwnerSerializer(serializers.ModelSerializer):
  class Meta(object):
    model = User
    fields = ['username']

class DumplingSerializer(serializers.ModelSerializer):
  owner = OwnerSerializer(read_only=True)
  tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all(), required=False)
  class Meta:
    model = Dumpling
    fields = ['id', 'name', 'description', 'origin', 'tags', 'owner', 'imageUrl']

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

class UserSerializer(serializers.ModelSerializer):
  # #email = serializers.EmailField(
  #   required=True,
  #   validators=[UniqueValidator(queryset.User.objects.all())]
  # )
  # #username = serializers.CharField(
  #   validators=[UniqueValidator(queryset=User.objects.all())]
  # )
  # password = serializers.CharField(min_length=8)
  class Meta(object):
    model = User
    fields = ['id', 'username', 'password', 'email']