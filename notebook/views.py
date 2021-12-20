from django.shortcuts import render, redirect
from .models import Notebook
import datetime

def note_list(request):
    notes = Notebook.objects.all().order_by('-created_at')
    return render(request, 'note/index.html', {'notes': notes})

def note_create(request):
    if request.method == 'POST':
        note_data = request.POST

        data = Notebook(
            note_title = note_data.get('note_title'),
            note_data = note_data.get('note_data'),
            created_at = datetime.datetime.now(),
            updated_at = datetime.datetime.now()
        )
        data.save()

        return redirect('notepage')

def note_update(request, pk):
    if request.method == 'POST':
        note_data = request.POST

        target_note = Notebook.objects.get(id = pk)

        target_note.updated_at = datetime.datetime.now()
        target_note.note_data = note_data.get('note_data')
        target_note.save()
        
        return redirect('notepage')

def note_delete(request, pk):
    target_note = Notebook.objects.get(id = pk)
    target_note.delete()

    return redirect('notepage')
