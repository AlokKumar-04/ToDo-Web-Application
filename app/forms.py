from django import forms
from app.models import *

class TaskForm(forms.ModelForm):
    due_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        required=False
    )
    
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date']