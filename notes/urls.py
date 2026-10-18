from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.NoteListView.as_view(), name='list'),
    path('<int:pk>/', views.NoteDetailView.as_view(), name='detail'),
    path('fbv/', views.note_list_fbv, name='list_fbv'),
    path('fbv/<int:pk>/', views.note_detail_fbv, name='detail_fbv'),
]
