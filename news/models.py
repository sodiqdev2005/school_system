from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    body = RichTextField(blank=False, null=False)
    image_news = models.ImageField(null=False, blank=False, upload_to="images/")
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')

class Comments(models.Model):
    article = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=200)
    comment_author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('news')