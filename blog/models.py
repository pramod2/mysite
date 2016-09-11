from __future__ import unicode_literals
from django.db import models
from django.db.models import permalink
from django.utils import timezone
from tinymce.models import HTMLField

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"

    @permalink
    def get_absolute_url(self):
        return ('view_blog_category', None, { 'slug': self.slug })


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    categories = models.ManyToManyField(Category)
    created_date = models.DateTimeField(db_index=True, auto_now_add=True)
    last_updated = models.DateTimeField(db_index=True, auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)
    is_published = models.BooleanField(default=False)
    #category = models.ForeignKey(Category, on_delete=models.SET_NULL)

    def publish(self):
        self.published_date = timezone.now()
        self.is_published = True
        self.save()

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })

    def __str__(self):
        return self.title

