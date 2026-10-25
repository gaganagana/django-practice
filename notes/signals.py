import logging
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Note

logger = logging.getLogger('notes.signals')


@receiver(post_save, sender=Note)
def note_saved_handler(sender, instance, created, **kwargs):
    """Signal receiver triggered when a Note instance is saved."""
    action = "Created" if created else "Updated"
    logger.info(f"Note {action}: ID={instance.pk}, Title='{instance.title}'")


@receiver(post_delete, sender=Note)
def note_deleted_handler(sender, instance, **kwargs):
    """Signal receiver triggered when a Note instance is deleted."""
    logger.info(f"Note Deleted: ID={instance.pk}, Title='{instance.title}'")
