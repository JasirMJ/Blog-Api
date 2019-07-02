from django.contrib.auth.models import User, Group
from rest_framework import serializers
from blog.models import Post,Tag, PostTagRelation


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class PostSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('__all__')

class TagSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('__all__')

class PostTagRelationSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PostTagRelation
        fields = ('__all__')
