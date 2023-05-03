from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import generic

from studying_portal.notes.forms import NotesForm
from studying_portal.notes.models import Notes


def home(request):
    return render(request, 'core/home.html')


def notes(request):
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            note = Notes(user=request.user, title=request.POST['title'], description=request.POST['description'])
            note.save()
        messages.success(request, f"Note added from {request.user.username} successfully")
    else:
        form = NotesForm()

    # TODO: Here you have to fix when you have users
    # To show you notes only for current user
    user_notes = Notes.objects.filter(user=request.user)

    context = {
        "notes": user_notes,
        'form': form,
    }
    return render(request, 'notes/notes.html', context)


def delete_note(request, pk):
    Notes.objects.get(pk=pk).delete()
    return redirect('notes')


class NoteDetailsView(generic.DetailView):
    model = Notes
