from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    CreateView
)
from .models import Note


def home(request):
    context = {
        'notes': Note.objects.all()
    }
    return render(request, 'notes/home.html', context)


class NoteListView(ListView):
    model = Note
    template_name = 'notes/home.html'
    context_object_name = 'notes'
    ordering = ['-date_added']


class NoteDetailView(DetailView):
    model = Note


class NoteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Note
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        note = self.get_object()
        if self.request.user == note.author:
            return True
        return False


class NoteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Note
    success_url = '/'

    def test_func(self):
        note = self.get_object()
        if self.request.user == note.author:
            return True
        return False


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    return render(request, 'notes/about.html', {'title': 'About'})