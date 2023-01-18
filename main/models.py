from django.db import models

class Word(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    create_time = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
