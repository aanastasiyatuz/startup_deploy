from django.db import models


class PlaceMixin(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)


class CommentMixin(models.Model):
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
