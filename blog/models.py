from __future__ import unicode_literals
from django.db import models
from django.db.models import permalink

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
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
    posted_date = models.DateTimeField(db_index=True, auto_now_add=True)
    categories = models.ManyToManyField(Category)
    #category = models.ForeignKey(Category, on_delete=models.SET_NULL)

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })

    def __unicode__(self):
        return self.title
