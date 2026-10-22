from django.shortcuts import render, get_object_or_404, redirect
from .models import Note, Category
from .forms import NoteForm


def note_list_fbv(request):
    """Function-based view for learning Django FBV request-response flow."""
    notes = Note.objects.filter(is_archived=False)
    categories = Category.objects.all()
    return render(request, 'notes/note_list.html', {
        'notes': notes,
        'categories': categories,
        'view_type': 'Function-Based View',
    })


def note_detail_fbv(request, pk):
    """Function-based view to display a single note by primary key."""
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'notes/note_detail.html', {
        'note': note,
        'view_type': 'Function-Based View',
    })

from django.db.models import Q
from django.views.generic import ListView, DetailView


class NoteListView(ListView):
    """Generic Class-Based View for listing active notes with pagination."""
    model = Note
    template_name = 'notes/note_list.html'
    context_object_name = 'notes'
    paginate_by = 6

    def get_queryset(self):
        qs = Note.objects.filter(is_archived=False).select_related('category')
        q = self.request.GET.get('q', '').strip()
        if q:
            qs = qs.filter(Q(title__icontains=q) | Q(content__icontains=q))
        priority = self.request.GET.get('priority', '').strip()
        if priority:
            qs = qs.filter(priority=priority)
        category_slug = self.request.GET.get('category', '').strip()
        if category_slug:
            qs = qs.filter(category__slug=category_slug)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['total_count'] = Note.objects.count()
        context['active_count'] = Note.objects.filter(is_archived=False).count()
        context['view_type'] = 'Class-Based View (ListView)'
        return context


class NoteDetailView(DetailView):
    """Generic Class-Based View for viewing note details."""
    model = Note
    template_name = 'notes/note_detail.html'
    context_object_name = 'note'

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


class NoteCreateView(SuccessMessageMixin, CreateView):
    """Generic Class-Based View for creating new notes."""
    model = Note
    form_class = NoteForm
    template_name = 'notes/note_form.html'
    success_message = 'Note "%(title)s" was successfully created!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Create New Note'
        return context


class NoteUpdateView(SuccessMessageMixin, UpdateView):
    """Generic Class-Based View for editing existing notes."""
    model = Note
    form_class = NoteForm
    template_name = 'notes/note_form.html'
    success_message = 'Note "%(title)s" was successfully updated!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Update Note'
        return context


class NoteDeleteView(DeleteView):
    """Generic Class-Based View for confirming and deleting notes."""
    model = Note
    template_name = 'notes/note_confirm_delete.html'
    success_url = reverse_lazy('notes:list')
    context_object_name = 'note'
