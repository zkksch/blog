from rest_framework import viewsets

from blog.apps.post import models
from blog.apps.post import serializers


class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer


class PostVoteViewSet(viewsets.ModelViewSet):
    queryset = models.PostVote.objects.all()
    serializer_class = serializers.PostVoteSerializer


class PostTagViewSet(viewsets.ModelViewSet):
    queryset = models.PostTag.objects.all()
    serializer_class = serializers.PostTagSerializer
