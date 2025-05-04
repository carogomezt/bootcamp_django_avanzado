from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True)
    published_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
