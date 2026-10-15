from django.contrib import admin
from .models import Category, Note


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at', 'note_count')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

    def note_count(self, obj):
        return obj.notes.count()
    note_count.short_description = 'Total Notes'


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'priority', 'is_archived', 'word_count', 'created_at')
    list_filter = ('priority', 'is_archived', 'category', 'created_at')
    search_fields = ('title', 'content')
    list_editable = ('priority', 'is_archived')
    date_hierarchy = 'created_at'
    actions = ['mark_as_archived', 'mark_as_active']

    @admin.action(description='Mark selected notes as Archived')
    def mark_as_archived(self, request, queryset):
        updated = queryset.update(is_archived=True)
        self.message_user(request, f'{updated} note(s) successfully marked as archived.')

    @admin.action(description='Mark selected notes as Active')
    def mark_as_active(self, request, queryset):
        updated = queryset.update(is_archived=False)
        self.message_user(request, f'{updated} note(s) successfully restored to active.')
