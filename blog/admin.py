from django.contrib import admin
from blog.models import Post, Category
from django.utils import timezone
from django.core.urlresolvers import reverse
from django import forms
from blog.models import Post
from tinymce.widgets import TinyMCE


class PostForm(forms.ModelForm):
    #body = forms.CharField(widget=TinyMCE(mce_attrs={'external_link_list_url': reverse('tinymce.views.flatpages_link_list')}))
    body = forms.CharField(
        widget=TinyMCE())


def publish_post(modeladmin, request, queryset):
    queryset.update(published_date=timezone.now())
    queryset.update(is_published=True)

publish_post.short_description = "Mark selected posts as published"

class PostAdmin(admin.ModelAdmin):
    exclude = ['posted_date']
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'created_date', 'last_updated', 'is_published')
    actions = [publish_post]
    form = PostForm


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)