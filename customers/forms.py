from .models import Customer
from django import forms


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = []

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
            }),
            'priority': forms.CheckboxInput(attrs={
                'class': 'form-control form-control-sm',
            }),
            'country': forms.Select(attrs={
                'class': 'form-control form-control-sm',
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
            }),
            'address_2': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
            }),
            'website': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
            }),
            'sap': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
            }),
            'responsible': forms.Select(attrs={
                'class': 'form-control form-control-sm',
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control form-control-sm',
                'rows': 3
            }),
        }