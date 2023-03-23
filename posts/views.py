from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Post
from django import reverse_lazy


class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post

class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post

class PostCreateView(CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "subtitle", "body", "author"]

class PostDeleteView(DeleteView):
    template_name = "post/delete.html"
    model = Post
    success_url = reverse_lazy("list")

class PostUpdateView(UpdateView):
    template_name = "post/update.html"
    model = Post
    fields = ["title", "subtitle", "body"]