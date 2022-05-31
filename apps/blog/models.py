from django.db import models
from apps.products.models import Category


class Tag(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=221)
    image = models.ImageField(upload_to='blog/')
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
