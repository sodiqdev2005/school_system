from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
# Create your models here.

class TeacherData(models.Model):
    teacher_photo = models.ImageField(null=False, blank=False, upload_to="images/")
    teacherfio = models.CharField(max_length=100)
    kasbi = models.CharField(max_length=100)
    teacher_info = RichTextField()

    def __str__(self):
        return self.teacherfio

    def get_absolute_url(self):
        return reverse('teacher_info')