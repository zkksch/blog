from rest_framework import viewsets

from blog.apps.comment.models import Comment
from blog.apps.comment.serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
