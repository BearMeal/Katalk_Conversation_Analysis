from django.db import models

# Create your models here.

class Todo(models.Model):
    title= models.CharField(max_length=50)
    description= models.TextField()
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    completed= models.BooleanField(default=False)
    important = models.BooleanField(default=False)

    def __str__(self):
        return self.title
