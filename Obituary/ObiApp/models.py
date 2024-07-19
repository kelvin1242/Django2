from django.db import models
from django.utils.text import slugify

class Obituary(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    date_of_death = models.DateField()
    content = models.TextField()
    author = models.CharField(max_length=100)
    submission_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            if self.submission_date:
                self.slug = slugify(self.name + '-' + str(self.submission_date.timestamp()))
            else:
                # Handle case where submission_date is None
                self.slug = slugify(self.name + '-' + 'no-date')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

# Create your models here.
