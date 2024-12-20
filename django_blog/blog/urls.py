from django.urls import path
from django.contrib.auth import views as auth_views
from taggit import posts_by_tag
from . import views
from .views import (
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView, CommentCreateView,
    CommentUpdateView, CommentDeleteView, search_posts, 
    PostByTagListView
)


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path("post/new/", PostCreateView.as_view(), name='post-create'),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name='post-update'),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name='post-delete'),
    path("post/<int:pk>/comments/new/", CommentCreateView, name='CommentCreateView'),
    path("comment/<int:pk>/update/", CommentUpdateView.as_view(), name='comment-update'),
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name='comment-delete'),
    path('search/', search_posts, name='search-posts'),
    path("tags/<slug:tag_slug>/", PostByTagListView.as_view(), name='posts-by-tag'),
]
