from rest_framework import serializers

from blog.apps.tag import models


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Tag

        fields = (
            'id',
            'created',
            'modified',
            'user',
            'tag',
        )

        read_only_fields = (
            'id',
            'created',
            'modified',
            'user',
        )

    def get_queryset(self):
        queryset = super(TagSerializer, self).get_queryset()
        return queryset
