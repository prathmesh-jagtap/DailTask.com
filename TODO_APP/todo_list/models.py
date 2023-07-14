from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    """This class stroes the task info in databased by user

    Args:
        models (built-in): models
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200, null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)  # time and date

    def __str__(self) -> str:
        return self.title

    class Meta:
        order_with_respect_to = 'user'
