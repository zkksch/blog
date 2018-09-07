from rest_framework import viewsets

from blog.apps.tag.models import Tag
from blog.apps.tag.serializers import TagSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
