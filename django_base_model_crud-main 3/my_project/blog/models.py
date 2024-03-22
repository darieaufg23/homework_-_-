from typing import Iterable
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return f"{self.name}"


class Post(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField(max_length=450)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True, editable=False)

    def __str__(self):
        return f"Post: {self.title} :=> {self.text}"


class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(max_length=450)

    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True, editable=False)


class PostSettings(models.Model):
    title_len = models.IntegerField(default=40)
    text_len = models.IntegerField(default=80)

    def save(self, *args, **kwargs) -> None:
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj, created
    
