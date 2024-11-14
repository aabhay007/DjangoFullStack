# myapp/models.py
from django.db import models

#Book Model
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    published_date = models.DateField()

    def __str__(self):
        return self.title
