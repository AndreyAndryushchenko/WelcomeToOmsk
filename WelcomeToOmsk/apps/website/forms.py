from django import forms
from django.forms import TextInput, EmailInput, Textarea


class ContactForm(forms.Form):
    name = forms.CharField(max_length=300, widget=TextInput(attrs={
        'class': 'your-name',
        'placeholder': 'Ваше имя',
        'autocomplete': 'off'
    }))
    email = forms.EmailField(widget=EmailInput(attrs={
        'class': 'your-email',
        'placeholder': 'Ваш электронный адрес',
        'autocomplete': 'off'
    }))
    message = forms.CharField(widget=Textarea(attrs={
        'class': 'your-message',
        'placeholder': 'Сообщение'
    }))
