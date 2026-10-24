import math
from django import template

register = template.Library()


@register.filter(name='priority_badge')
def priority_badge(priority):
    """Returns CSS badge class according to priority level."""
    mapping = {
        'high': 'badge-priority-high',
        'medium': 'badge-priority-medium',
        'low': 'badge-priority-low',
    }
    return mapping.get(str(priority).lower(), 'bg-secondary')


@register.filter(name='reading_time')
def reading_time(content):
    """Calculates estimated reading time in minutes (approx. 200 words/min)."""
    if not content:
        return '1 min'
    words = len(content.split())
    minutes = math.ceil(words / 200)
    return f"{minutes} min read"
