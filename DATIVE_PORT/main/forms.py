from django import forms
from .models import Message, Service


class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'phone', 'company', 'service', 'subject', 'message', 'budget']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name*', 'required': True}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email*', 'required': True}),
            'phone': forms.TextInput(attrs={'placeholder': 'Your Phone'}),
            'company': forms.TextInput(attrs={'placeholder': 'Your Company'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject*', 'required': True}),
            'message': forms.Textarea(attrs={'placeholder': 'Your Message*', 'rows': 5, 'required': True}),
            'budget': forms.TextInput(attrs={'placeholder': 'Estimated Budget'}),
        }