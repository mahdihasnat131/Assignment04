from django.db import models
from task.models import Task


# Create your models here.

class Category(models.Model):
    category_name=models.CharField(max_length=12)
    task_category=models.ForeignKey(Task, on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.category_name