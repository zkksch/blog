from rest_framework import serializers

from blog.apps.comment import models


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Comment

        fields = (
            'id',
            'created',
            'modified',
            'user',
            'post',
            'content',
            'parent',
        )

        read_only_fields = (
            'id',
            'created',
            'modified',
            'user',
        )
