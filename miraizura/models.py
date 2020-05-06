from accounts.models import CustomUser
from django.db import models

class Diary(models.Model):

    user = models.ForeignKey(CustomUser, verbose_name='user', on_delete=models.PROTECT)
    title = models.CharField(verbose_name='title', max_length=40)
    content = models.TextField(verbose_name='content', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='created date', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='updated date', auto_now=True)

    class Meta:
        verbose_name_plural = 'Diary'

        def __str__(self):
            return self.title
