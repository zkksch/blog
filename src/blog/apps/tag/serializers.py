from rest_framework import serializers

from blog.apps.tag import models


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = (
            'created', 'modified', 'user', 'tag')
