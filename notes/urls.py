# notes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # URL for the note list view
    path('', views.note_list, name='note_list'),
    # URL for the note detail view 
    path('note/<int:pk>/', views.note_detail, name='note_detail'),
    # URL for the note create view
    path('note/new/', views.note_create, name='note_create'),
    # URL for the note update view
    path('note/<int:pk>/edit/', views.note_update, name='note_update'),
    # URL for the note delete view
    path('note/<int:pk>/delete/', views.note_delete, name='note_delete'),
    # URL for the post list view
    path('posts/', views.post_list, name='post_list'),
    # URL for the post detail view
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # URL for the post create view
    path('post/new/', views.post_create, name='post_create'),
    # URL for the post update view
    path('post/<int:pk>/edit/', views.post_update, name='post_update'),
    # URL for the post delete view
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
]
