from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True)
    description = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('notes:category_notes', kwargs={'slug': self.slug})


class Note(models.Model):
    PRIORITY_LOW = 'low'
    PRIORITY_MEDIUM = 'medium'
    PRIORITY_HIGH = 'high'

    PRIORITY_CHOICES = [
        (PRIORITY_LOW, 'Low Priority'),
        (PRIORITY_MEDIUM, 'Medium Priority'),
        (PRIORITY_HIGH, 'High Priority'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes', null=True, blank=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='notes'
    )
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default=PRIORITY_MEDIUM
    )
    is_archived = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['priority']),
            models.Index(fields=['is_archived']),
        ]

    def __str__(self):
        return f"{self.title} ({self.get_priority_display()})"

    def get_absolute_url(self):
        return reverse('notes:detail', kwargs={'pk': self.pk})

    @property
    def word_count(self):
        return len(self.content.split()) if self.content else 0

    @property
    def summary(self):
        if len(self.content) <= 120:
            return self.content
        return self.content[:117] + '...'
