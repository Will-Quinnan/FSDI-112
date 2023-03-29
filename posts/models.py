from django.db import models
from django.urls import reverse

from django.contrib.auth import urls, get_user_model

# Create your models here.

class Status(models.Model):
    name= models.CharField(max_length=128)
    description = models.TextField()

    def __str_(self):
        return self.name
class Post(models.Model):
    title = models.CharField(max_length=256)
    subtitle = models.CharField(max_length=256)
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE
    )

    def _str_(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', args=(self.id))
