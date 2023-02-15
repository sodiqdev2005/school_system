from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.
class Contest(models.Model):
    title = models.CharField(max_length=200)
    image_contest = models.ImageField(null=False, blank=False, upload_to='images/')
    body = RichTextField()
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')