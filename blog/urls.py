from django.urls import path
from .views import PostListView, PostDetailView, post_share

app_name = 'blog'
urlpatterns = [
    path("", PostListView.as_view(), name='home'),
    path("page/<int:page>", PostListView.as_view(), name='home'),
    path("post/<int:id>/", PostDetailView.as_view(), name='post_detail'),
    path("<int:post_id>/share/", post_share, name='post_share'),
]