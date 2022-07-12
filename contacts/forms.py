from .models import Contact
from django import forms


class ContactForm(forms.ModelForm):
    def clean_customer(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.customer
        else:
            return self.cleaned_data['customer']

    class Meta:
        model = Contact
        fields = '__all__'
        exclude = []

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
            }),
            'surname': forms.TextInput(attrs={
                    'class': 'form-control form-control-sm',
                }),
            'department': forms.Select(attrs={
                    'class': 'form-control form-control-sm select2',
                }),
            'position': forms.TextInput(attrs={
                        'class': 'form-control form-control-sm',
                    }),
            'phone': forms.TextInput(attrs={
                        'class': 'form-control form-control-sm',
                    }),
            'phone_2': forms.TextInput(attrs={
                        'class': 'form-control form-control-sm',
                    }),
            'email': forms.TextInput(attrs={
                        'class': 'form-control form-control-sm',
                    }),
            'email_2': forms.TextInput(attrs={
                        'class': 'form-control form-control-sm',
                    }),
            'customer': forms.Select(attrs={
                        'class': 'form-control form-control-sm select2',
                    }),
            'actual': forms.CheckboxInput(attrs={
                        'class': 'form-control form-control-sm',
                    }),
            'emailing': forms.CheckboxInput(attrs={
                        'class': 'form-control form-control-sm',
                    }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control form-control-sm',
                'rows': 4
            }),
        }