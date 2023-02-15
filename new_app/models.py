from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=False, null=False)
    published = models.DateField(auto_now_add=True)
    def __str__(self):
        return str(self.author) + self.title

    def get_absolute_url(self):
        return reverse('home')

