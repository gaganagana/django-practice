from django import forms
from .models import Category, Note


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Work, Ideas, Python'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'unique-slug'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'category', 'priority', 'content', 'is_archived']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter note title'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': 'Write your thoughts or code snippets here...'}),
            'is_archived': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title', '').strip()
        if len(title) < 3:
            raise forms.ValidationError('Title must be at least 3 characters long.')
        if title.lower() in ['test', 'untitled', 'dummy']:
            raise forms.ValidationError('Please provide a meaningful title.')
        return title
