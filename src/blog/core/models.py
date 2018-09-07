from django.db import models
from django.utils.translation import ugettext_lazy as _


class BaseModel(models.Model):
    created = models.DateTimeField(
        _('Created'), auto_now_add=True, null=False, blank=False)

    modified = models.DateTimeField(
        _('Modified'), auto_now=True, null=False, blank=False)

    @property
    def _info(self):
        return ''

    def __str__(self):
        return f'{self.__class__.__name__} (id={self.id}) {{ {self._info} }}'

    class Meta:
        abstract = True
