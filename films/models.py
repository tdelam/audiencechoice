import datetime

from django.db import models

from markdown import markdown


class Category(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('film_category', (), { 'category_slug': self.slug })


class Film(models.Model):
    title = models.CharField(max_length=250)
    thumb = models.ImageField(upload_to="uploads/")
    director = models.CharField(max_length=150)
    year = models.CharField(max_length=25)
    country = models.CharField(max_length=50)
    runtime = models.CharField(max_length=50)
    category = models.ForeignKey(Category)
    active = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title
