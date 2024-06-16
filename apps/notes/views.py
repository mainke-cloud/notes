from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import NotesForm
from .models import Notes

@login_required
def index(request):
    notes_list = Notes.objects.filter(user=request.user)
    return render(request, "index.html",locals())

@login_required
def add(request):
    form = NotesForm()
    if request.method == "POST":
        data = request.POST.copy()
        data['user'] = request.user
        form = NotesForm(data)
        if form.is_valid():
            form.save()
            return redirect("notes-index")
    return render(request, "add.html", locals())

@login_required
def edit(request, id):
    note = Notes.objects.get(id=id)
    form = NotesForm(instance=note)
    if request.method == "POST":
        data = request.POST.copy()
        data['user'] = request.user
        form = NotesForm(data, instance=note)
        if form.is_valid():
            form.save()
            return redirect("notes-index")
    return render(request, "edit.html", locals())

@login_required
def delete(request, id):
    notes = Notes.objects.get(id=id)
    notes.delete()
    return redirect("notes-index")
