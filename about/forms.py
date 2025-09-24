from django import forms
from .models import CollaborateRequest


class CollaborateForm(forms.ModelForm):
    class Meta:
        model = CollaborateRequest
        fields = ['name', 'email', 'message']
        labels = {
            'name': 'Your Name',
            'email': 'Your Email Address',
            'message': 'Tell us about your collaboration idea'
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter your full name',
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'your.email@example.com',
                'class': 'form-control'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Describe your collaboration idea or project...',
                'rows': 5,
                'class': 'form-control'
            })
        }
