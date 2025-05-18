from django.contrib.auth import get_user_model
from account.models import *
from django.db import models


# Create your models here.

class Tag(models.Model):
    tag_name = models.CharField(max_length=120)

    def __str__(self):
        return self.tag_name


class Category(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name


class Post(models.Model):
    post_image = models.ImageField(upload_to='post_images', null=True, blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)
    post_status = models.BooleanField(default=False)
    post_views = models.IntegerField(default=0)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.subject
