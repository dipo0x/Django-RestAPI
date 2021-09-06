from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')

    def __str__(self):
        return self.title