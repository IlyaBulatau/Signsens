from django.db import models
from django.urls import reverse

class Word(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    create_time = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('create_time',)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('detail_word', kwargs={'word_slug': self.slug})