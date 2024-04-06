from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Task(models.Model):
    # Task 상태에 대한 Enum 클래스 정의
    class Status(models.TextChoices):
        TODO = 'TD', _('To Do')
        IN_PROGRESS = 'IP', _('In Progress')
        DONE = 'DN', _('Done')

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('User'))
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    description = models.TextField(blank=True, verbose_name=_('Description'))
    start_date = models.DateField(verbose_name=_('Start Date'))
    end_date = models.DateField(verbose_name=_('End Date'))
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.TODO, verbose_name=_('Status'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    class Meta:
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')

    def __str__(self):
        return self.title
