from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from blog.core.models import BaseModel


class Tag(BaseModel):
    user = models.ForeignKey(
        User, verbose_name=_('Created by'), related_name='tags',
        null=True, blank=True, on_delete=models.SET_NULL)

    tag = models.CharField(
        verbose_name=_('Tag'), max_length=64, null=False, blank=False)

    @property
    def _info(self):
        return (
            f'Tag "{self.tag}" created by {self.user} '
            f'on {self.created: %d.%m.%Y}'
        )
