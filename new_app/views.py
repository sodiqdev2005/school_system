from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy
# Create your views here.

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['id']

class ArticleDetail(DetailView):
    model = Post
    template_name = 'detail.html'

class PostView(CreateView):
    model = Post
    template_name = 'post.html'
    fields = '__all__'

class EditPost(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = '__all__'

class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

