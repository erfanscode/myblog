from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.conf import settings
from .models import Post

# Create your views here.
class PostListView(ListView):
    queryset        = Post.published.all()
    template_name   = 'blog/list.html'
    context_object_name = "posts"
    paginate_by = 1

class PostDetailView(DetailView):
    template_name = 'blog/detail.html'
    def get_object(self):
        id = self.kwargs.get('id')
        post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)

        return post