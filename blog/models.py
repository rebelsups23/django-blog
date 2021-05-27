from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(("Title"), max_length=200)
    text = models.TextField(("Content"))
    image = models.ImageField(("Image"), upload_to="post/images", null=True, blank=True)
    created_date = models.DateTimeField(('Created Date'), auto_now_add=True)
    published_date = models.DateTimeField(("Published Date"), auto_now=True)

    def __str__(self):
        return self.title


