from django.contrib import admin
from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.CharField(max_length=200)
    like_count = models.IntegerField(default=0)

    @admin.display(
        boolean=True,
        description="Is popular?",
        ordering='like_count'
    )
    def is_popular(self):
        return self.like_count >= 100

    def __str__(self):
        return self.title

