from django.contrib.auth.models import User
from rest_framework import serializers

from tut_drf.models import Snippet

class SnippetSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        # 보여질 필드 선정
        fields = ['id', 'owner', 'title', 'code', 'linenos', 'language', 'style',]

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']