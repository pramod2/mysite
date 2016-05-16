from django.contrib import admin
from blog.models import Post, Category


class PostAdmin(admin.ModelAdmin):
    exclude = ['posted_date']
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'posted_date')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)