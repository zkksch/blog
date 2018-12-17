from rest_framework import serializers

from blog.apps.post import models
from blog.apps.tag.models import Tag


class PostTagSerializer(serializers.PrimaryKeyRelatedField,
                        serializers.ModelSerializer):

    class Meta:
        models = models.PostTag

        fields = (
            'id',
            'created',
            'modified',
            'tag',
            'post'
        )

        read_only_fields = (
            'id',
            'created',
            'modified',
        )


class PostSerializer(serializers.ModelSerializer):

    # tags = PostTagSerializer(
    #     many=True,
    #     queryset=Tag.objects.all(),
    # )

    tag_list = serializers.CharField()

    class Meta:
        model = models.Post

        fields = (
            'id',
            'created',
            'modified',
            'user',
            'title',
            'tags',
            'tag_list',
            'content',
        )

        read_only_fields = (
            'id',
            'created',
            'modified',
            'user',
        )

    def save(self, **kwargs):
        tags = self.validated_data.pop('tags', [])

        _tags = []

        for tag in tags:
            models.PostTag.objects.filter(post=self.instance).delete()
            models.PostTag.objects.create(post=self.instance, tag=tag)

        return super(PostSerializer, self).save(**kwargs)
