from django.contrib.auth import get_user_model
from account.models import *
from django.db import models


# Create your models here.


class Tag(models.Model):
    tag_name = models.CharField(max_length=255)

    def __str__(self):
        return self.tag_name


class Category(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    post_image = models.ImageField(upload_to='post_images')
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    comments = models.ManyToManyField(Comments, blank=True)
    post_status = models.BooleanField(default=False)
    post_views = models.IntegerField(default=0)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
