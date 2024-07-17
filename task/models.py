from django.db import models
# from category.models import Category

# Create your models here.

class Task(models.Model):
    task_title=models.CharField(max_length=12)
    task_desc=models.CharField(max_length=100)
    task_completion=models.BooleanField(default=False)
    task_assign=models.DateField()
    # category= models.ManyToManyField(Category)

    def __str__(self):
        return self.task_title