from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from seeyou.forms import PostForm
from seeyou.models import Post


class PostListView(ListView):
    model = Post
    # paginate_by = 4

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    templates = 'form.html'

class PostDetailView(DetailView):
    model = Post

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm

class PostDeleteView(DeleteView):
    model = Post