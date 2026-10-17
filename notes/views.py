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
