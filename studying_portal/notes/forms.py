from django.forms import models

from studying_portal.notes.models import Notes


class NotesForm(models.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'description']