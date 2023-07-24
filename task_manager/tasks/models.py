from django.db import models

from task_manager.status.models import Status
from task_manager.labels.models import Labels
from task_manager.users.models import User
from django.utils.translation import gettext_lazy as _


class Task(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    description = models.TextField(verbose_name=_('Description'))
    status = models.ForeignKey(Status,
                               on_delete=models.CASCADE,
                               verbose_name=_('Status'))
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='author_tasks',
                               verbose_name=_('Author'))
    executor = models.ForeignKey(User, on_delete=models.CASCADE,
                                 related_name='executor_tasks',
                                 verbose_name=_('Executor'))
    labels = models.ManyToManyField(Labels, verbose_name=_('Labels'),
                                    through='TaskLabel',
                                    related_name='Tasks',
                                    blank=True)

    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'tasks'


class TaskLabel(models.Model):
    """Link model for ManyToMany relation between Task and Label models."""

    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    label = models.ForeignKey(Labels, on_delete=models.PROTECT)
