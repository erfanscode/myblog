from django.urls import path
from .views import PostListView, PostDetailView

app_name = 'blog'
urlpatterns = [
    path("", PostListView.as_view(), name='home'),
    path("page/<int:page>", PostListView.as_view(), name='home'),
    path("post/<int:id>/", PostDetailView.as_view(), name='post_detail')
]