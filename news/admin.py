from django.contrib import admin
from .models import News,Comments
# Register your models here.

class CommentInLine(admin.TabularInline):
    model = Comments
    extra = 3

class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInLine]

admin.site.register(News, ArticleAdmin)
admin.site.register(Comments)