from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    # title = forms.CharField(label="Имя")
    # description = forms.CharField(label='Описание')
    # date = forms.DateTimeField(label="Дата")
    class Meta:
        model = Task
        fields = ['title', 'description']