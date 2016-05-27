from django.contrib import admin
from blog.models import Post, Category
from django.utils import timezone

def publish_post(modeladmin, request, queryset):
    queryset.update(published_date=timezone.now())
    queryset.update(is_published=True)
publish_post.short_description = "Mark selected posts as published"


class PostAdmin(admin.ModelAdmin):
    exclude = ['posted_date']
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'created_date', 'last_updated', 'is_published')
    actions = [publish_post]

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)