from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('fbv/', views.note_list_fbv, name='list_fbv'),
    path('fbv/<int:pk>/', views.note_detail_fbv, name='detail_fbv'),
]
