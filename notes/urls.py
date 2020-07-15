from django.urls import path
from .views import (
    NoteListView,
    NoteDetailView,
    NoteUpdateView,
    NoteDeleteView,
    NoteCreateView,
)
from . import views

urlpatterns = [
    path('', NoteListView.as_view(), name='notes-home'),
    path('about/', views.about, name='notes-about'),
    path('note/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
    path('note/<int:pk>/update/', NoteUpdateView.as_view(), name='note-update'),
    path('note/<int:pk>/delete/', NoteDeleteView.as_view(), name='note-delete'),
    path('note/new/', NoteCreateView.as_view(), name='note-create'),
]