from .models import Task
from django import forms


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['creator']

        widgets = {
            'description': forms.Textarea(attrs={
                'class': 'form-control form-control-sm',
                'rows': 4
            }),
            'result': forms.Textarea(attrs={
                'class': 'form-control form-control-sm',
                'rows': 4
            }),
            'reminder': forms.DateInput(attrs={
                'class': 'form-control form-control-sm',
                'type': 'date'
            }),
            'done': forms.CheckboxInput(attrs={
                'class': 'form-control form-control-sm',
            }),
            'responsible': forms.Select(attrs={
                'class': 'form-control form-control-sm',
            }),
            'customer': forms.Select(attrs={
                'class': 'form-control form-control-sm select2',
                'onchange': "linkedListUpload(this)",
            }),
            'contact': forms.Select(attrs={
                'class': 'form-control form-control-sm select2',
                'data-depend': 'customer',
            }),
            'project': forms.Select(attrs={
                'class': 'form-control form-control-sm select2',
                'data-depend': 'customer',
            }),
            'product': forms.Select(attrs={
                'class': 'form-control form-control-sm select2',
            }),
        }
