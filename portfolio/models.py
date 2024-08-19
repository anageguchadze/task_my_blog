from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    author = models.CharField(max_length=200)

class Person(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=100)

    def __str__(self):
        return self.title