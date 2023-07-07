from django.db import models
from django.contrib.auth.models import User
from status.models import Status
from labels.models import labels

class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()  # If you want to add a description field
    status = models.ForeignKey(Status, on_delete=models.CASCADE)  # Link to the Status model
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_tasks')  # Link to the User model
    executor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='executor_tasks')  # Link to the User model
    label = models.ForeignKey(labels, on_delete=models.CASCADE, null=True)  # Link to the Label model
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'tasks'