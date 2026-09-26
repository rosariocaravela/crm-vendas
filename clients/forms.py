from django import forms
from .models import Client, Interaction

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        exclude = ['created_by']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input w-full'}),
            'email': forms.EmailInput(attrs={'class': 'form-input w-full'}),
            'phone': forms.TextInput(attrs={'class': 'form-input w-full'}),
            'company': forms.TextInput(attrs={'class': 'form-input w-full'}),
            'address': forms.Textarea(attrs={'class': 'form-textarea w-full', 'rows': 3}),
            'notes': forms.Textarea(attrs={'class': 'form-textarea w-full', 'rows': 3}),
            'status': forms.Select(attrs={'class': 'form-select w-full'}),
        }

class InteractionForm(forms.ModelForm):
    class Meta:
        model = Interaction
        fields = ['type', 'description']
        widgets = {
            'type': forms.Select(attrs={'class': 'form-select w-full'}),
            'description': forms.Textarea(attrs={'class': 'form-textarea w-full', 'rows': 3, 'placeholder': 'Descreva a interação...'}),
        }
