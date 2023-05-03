from django import forms
from django.forms import models

from studying_portal.notes.models import Notes


class NotesForm(models.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'})

        }