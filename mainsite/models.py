from django.db import models

# Create your models here.

#Current SpecialSections, as of September 10, 2016 (the section names) are
#about_me
#thought_of_the_day
class SpecialSection(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    section_name = models.CharField(max_length=100)
    body = models.TextField()
    author = models.CharField(max_length=100, default="Pramod")
    created_date = models.DateTimeField(db_index=True, auto_now_add=True)
    last_updated = models.DateTimeField(db_index=True, auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)
    is_published = models.BooleanField(default=False)
    #category = models.ForeignKey(Category, on_delete=models.SET_NULL)

    def publish(self):
        self.published_date = timezone.now()
        self.is_published = True
        self.save()

    def __str__(self):
        return self.title