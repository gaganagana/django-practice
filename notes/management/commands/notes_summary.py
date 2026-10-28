from django.core.management.base import BaseCommand
from notes.models import Note, Category


class Command(BaseCommand):
    help = 'Displays a formatted terminal summary of current notes and category distribution'

    def handle(self, *args, **options):
        total_notes = Note.objects.count()
        active_notes = Note.objects.filter(is_archived=False).count()
        archived_notes = Note.objects.filter(is_archived=True).count()
        total_cats = Category.objects.count()

        self.stdout.write(self.style.SUCCESS('=== Django Practice: Notes Summary ==='))
        self.stdout.write(f"Total Notes: {total_notes} ({active_notes} active, {archived_notes} archived)")
        self.stdout.write(f"Categories:  {total_cats}")
        self.stdout.write('--------------------------------------')
        for cat in Category.objects.all():
            self.stdout.write(f" - {cat.name}: {cat.notes.count()} notes")
        self.stdout.write(self.style.SUCCESS('Done.'))
