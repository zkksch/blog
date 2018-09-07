from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from mptt.models import MPTTModel
from mptt.models import TreeForeignKey

from blog.apps.post.models import Post
from blog.core.models import BaseModel


class Comment(BaseModel, MPTTModel):
    user = models.ForeignKey(
        User, related_name='comments', verbose_name=_('Created by'),
        null=True, blank=True, on_delete=models.SET_NULL)

    post = models.ForeignKey(
        Post, related_name='comments', verbose_name=_('Post'),
        null=True, blank=True, on_delete=models.SET_NULL)

    content = models.TextField(
        verbose_name=_('Comment'),
        null=False, blank=False)

    parent = TreeForeignKey(
        'self', related_name='children', verbose_name=_('Parent comment'),
        on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def _info(self):
        return (
            f'Comment in post "{self.post}" commented by {self.user} '
            f'on {self.created: %d.%m.%Y}'
        )
