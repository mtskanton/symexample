from .models import Project
from django import forms


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        exclude = []

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control form-control-sm',
                'rows': 4
            }),
            'customer': forms.Select(attrs={
                'class': 'form-control form-control-sm select2',
                'onchange': "linkedListUpload(this)",
            }),
            'contact': forms.Select(attrs={
                'class': 'form-control form-control-sm select2',
                'data-depend': 'customer',
            }),
            'archive': forms.CheckboxInput(attrs={
                'class': 'form-control form-control-sm',
            }),
        }
