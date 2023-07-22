from django.db import models
from django.utils.translation import gettext_lazy


class Status(models.Model):
    name = models.CharField(verbose_name=gettext_lazy('Name'), max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'status'
