from rest_framework import serializers

from blog.apps.comment import models


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = (
            'created', 'modified', 'user', 'content', 'parent')
