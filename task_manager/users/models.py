from django.contrib.auth.models import AbstractUser
from django.urls import reverse


# Create your models here.
class User(AbstractUser):
    def get_absolute_url(self):
        return reverse('users:user_list')

    def __str__(self):
        return self.get_full_name()
