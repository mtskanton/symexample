from .models import Sample
from django import forms


class SampleForm(forms.ModelForm):
    class Meta:
        model = Sample
        fields = '__all__'
        exclude = ['status_date']

        widgets = {
            'product': forms.Select(attrs={
                'class': 'form-control form-control-sm select2',
            }),
            'amount': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
            }),
            'status': forms.Select(attrs={
                'class': 'form-control form-control-sm',
            }),
            'direct': forms.CheckboxInput(attrs={
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
            'important': forms.CheckboxInput(attrs={
                'class': 'form-control form-control-sm',
            }),
            'potential': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
            }),
            'pace': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
            }),
            'sent': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'type': 'date'
            }),
            'sent_data': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control form-control-sm',
                'rows': 2
            }),

        }
