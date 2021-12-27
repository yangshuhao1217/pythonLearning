"""Defines URL patterns for blogs."""

from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all posts.
    path('posts/', views.posts, name='posts'),
    # Detail page for a single post.
    path('posts/<int:post_id>/', views.post, name='post'),
    # Page for adding a new post.
    path('new_post/', views.new_post, name='new_post'),
    # Page for adding a new entry.
    path('new_entry/<int:post_id>/', views.new_entry, name='new_entry'),
    # Page for editing an entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]