from django.shortcuts import render
from .models import News
from .models import Comments
from django.views.generic import ListView, DetailView, CreateView
# Create your views here.

class NewsView(ListView):
    model = News
    template_name = 'news.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class DetailNewsView(DetailView):
    model = News
    template_name = 'article_detail.html'

    def get_context_data(self, *args, **kwargs):
        # Call the base implementation first to get a context
        context = super(DetailNewsView,self).get_context_data(*args, **kwargs)
        # Add in a QuerySet of all the books
        return context

class NewComment(CreateView):
    model = Comments
    template_name = 'article_comments.html'
    fields = '__all__'