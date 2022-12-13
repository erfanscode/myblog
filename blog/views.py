from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.views.generic import ListView, DetailView, FormView, TemplateView
from environs import Env
from .models import Post
from .forms import EmailPostForm

env = Env()
env.read_env()

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


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            clear_data  = form.cleaned_data
            post_url    = request.build_absolute_uri(post.get_absolute_url())
            subject     = f"{clear_data['name']} recommends you read {post.title}"
            message     = f"Read {post.title} at {post_url}\n\n {clear_data['name']}\'s comments: {clear_data['comments']}"
            send_mail(subject, message, env("DJANGO_EMAIL_HOST_USER"), [clear_data['to']])
            sent        = True
    
    else:
        form = EmailPostForm()
    return render(request, 'blog/share.html', {'post':post, 'form':form, 'sent':sent})


# class PostShareView(FormView):
#     template_name = 'blog/share.html'
#     form_class = EmailPostForm
#     success_url = reverse_lazy('blog:post_share')
#     context_object_name = "post"
    
#     def get_object(self):
#         post_id = self.kwargs.get('post_id')
#         post_u = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
        
#     sent = False

#     def form_valid(self, form):
#         post_url = request.build_absolute_uri(post.get_absolute_url())
#         form.send()
#         return super().form_valid(form)


# class PostShareSuccessView(TemplateView):
#     template_name = 'blog/success.html'