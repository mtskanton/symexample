from .models import Product
from django import forms


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = []

        widgets = {
            'category': forms.Select(attrs={
                'class': 'form-control form-control-sm',
            }),
            'subcategory': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
            }),
            'phn': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
            }),
            'priority': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
            }),
            'number': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
            }),
            'properties': forms.Textarea(attrs={
                'class': 'form-control form-control-sm',
                'rows': 17
            }),
            'inci': forms.Textarea(attrs={
                'class': 'form-control form-control-sm',
                'rows': 1
            }),
            'dosage': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
            }),
            'color': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
            }),
            'form': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
            }),
            'solubility': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
            }),
            'registration': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control form-control-sm',
                'rows': 4
            }),
            'actual': forms.CheckboxInput(attrs={
                'class': 'form-control form-control-sm',
            }),
            'sanctioned': forms.Select(attrs={
                'class': 'form-control form-control-sm',
            }),
        }