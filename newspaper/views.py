from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

from .models import Post
# Create your views here.

class HomeView(ListView):
    template_name = 'home.html'
    model = Post

class DetailedView(DetailView):
    template_name = 'details.html'
    model = Post

class BlogCreateView(CreateView):
    template_name = 'add.html'
    model = Post
    fields = ['title', 'author' , 'body']

class BlogUpdateView(UpdateView):
    template_name = 'update.html'
    model = Post
    fields = ['title', 'author', 'body']

class BlogDeleteView(DeleteView):
    template_name = 'delete.html'
    model = Post
    fields = ['title', 'author', 'body']
    success_url = reverse_lazy('home')