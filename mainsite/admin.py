from django.contrib import admin
from mainsite.models import SpecialSection
from django.utils import timezone
from django import forms
from tinymce.widgets import TinyMCE

# Register your models here.
class SpecialSectionForm(forms.ModelForm):
    #body = forms.CharField(widget=TinyMCE(mce_attrs={'external_link_list_url': reverse('tinymce.views.flatpages_link_list')}))
    body = forms.CharField(
        widget=TinyMCE())


def publish_section(modeladmin, request, queryset):
    queryset.update(published_date=timezone.now())
    queryset.update(is_published=True)

publish_section.short_description = "Mark selected section post as published"

class SpecialSectionAdmin(admin.ModelAdmin):
    exclude = ['posted_date']
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'created_date', 'last_updated', 'is_published', 'author')
    actions = [publish_section]
    form = SpecialSectionForm


# Register your models here.
admin.site.register(SpecialSection, SpecialSectionAdmin)