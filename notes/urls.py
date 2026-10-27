from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.NoteListView.as_view(), name='list'),
    path('<int:pk>/', views.NoteDetailView.as_view(), name='detail'),
    path('create/', views.NoteCreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.NoteUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.NoteDeleteView.as_view(), name='delete'),
    path('fbv/', views.note_list_fbv, name='list_fbv'),
    path('fbv/<int:pk>/', views.note_detail_fbv, name='detail_fbv'),
    path('api/notes/', views.note_api_list, name='api_list'),
    path('api/stats/', views.note_api_stats, name='api_stats'),
]
