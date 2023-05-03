from django.urls import path

from studying_portal.notes import views

urlpatterns = [
    path('', views.home, name='home'),

    path('notes/', views.notes, name='notes'),
    path('notes/<int:pk>/', views.delete_note, name='delete_note'),
    path('notes_details/<int:pk>/', views.NoteDetailsView.as_view(), name='notes_details'),
]
