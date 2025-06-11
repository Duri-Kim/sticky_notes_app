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
]