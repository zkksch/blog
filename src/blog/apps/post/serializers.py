from rest_framework import serializers

from blog.apps.post import models


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = (
            'created', 'modified', 'user', 'title', 'tags', 'content', 'votes')


class PostVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PostVote
        fields = (
            'created', 'modified', 'post', 'user', 'vote')


class PostTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PostTag
        fields = (
            'created', 'modified', 'post', 'tag')
