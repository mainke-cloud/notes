from django import forms
from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        exclude = ['created_date', 'edited_date']
        widgets = {'user': forms.HiddenInput()}
