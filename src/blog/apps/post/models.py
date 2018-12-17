from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from blog.apps.tag.models import Tag
from blog.core.models import BaseModel


class Post(BaseModel):
    user = models.ForeignKey(
        User, related_name='posts', verbose_name=_('Created by'),
        on_delete=models.CASCADE)

    tags = models.ManyToManyField(
        Tag, related_name='posts', verbose_name=_('Tags'),
        through='post.PostTag')

    title = models.CharField(
        max_length=100, verbose_name=_('Title'),
        null=False, blank=False)

    content = models.TextField(
        verbose_name=_('Post'),
        null=False, blank=False)

    @property
    def tag_list(self):
        return ', '.join(tag.tag for tag in self.tags.all())

    @tag_list.setter
    def tag_list(self, value):
        tags = []

        for tag in [tag.strip() for tag in value.split(',')]:
            try:
                tag = Tag.objects.get(tag=tag)
            except Tag.DoesNotExist:
                tag = Tag.objects.create(
                    tag=tag,
                    user=self.user
                )

            tags.append(tag)

        PostTag.objects.filter(post=self).delete()
        for tag in tags:
            PostTag.objects.create(post=self, tag=tag)

    @property
    def _info(self):
        return (
            f'"{self.title}" created by {self.user} '
            f'on {self.created: %d.%m.%Y}'
        )


class PostTag(BaseModel):
    post = models.ForeignKey(
        Post, verbose_name=_('Post'),
        null=False, blank=False, on_delete=models.CASCADE)

    tag = models.ForeignKey(
        Tag, verbose_name=_('Tag'),
        null=False, blank=False, on_delete=models.CASCADE)


class PostVote(BaseModel):

    LIKE = 1
    DISLIKE = -1

    VOTES = [
        (LIKE, _('Like')),
        (DISLIKE, _('Dislike')),
    ]

    post = models.ForeignKey(
        Post, related_name='votes', verbose_name=_('Post'),
        null=False, blank=False, on_delete=models.CASCADE)

    user = models.ForeignKey(
        User, related_name='votes', verbose_name=_('Voted by'),
        null=True, blank=True, on_delete=models.SET_NULL)

    vote = models.SmallIntegerField(
        choices=VOTES, verbose_name=_('Vote'),
        null=False, blank=False)

    @property
    def _info(self):
        return (
            f'{self.user} {self.get_vote_display().lower()}d "{self.post}" '
            f'on {self.created: %d.%m.%Y}'
        )
