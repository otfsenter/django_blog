from django.db import models

# Create your models here.
from django.urls import reverse


class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    category = models.CharField(max_length=200)
    date_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        verbose_name_plural = 'Blog'

    # def get_absolute_url(self):
    #     return reverse('blog:detail', kwargs={'slug', self.id})
