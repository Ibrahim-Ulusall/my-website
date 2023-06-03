from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    firstName = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control m-3',
        'placeholder':'Adınız'
    }))
    lastName = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control m-3',
        'placeholder':'Soyadınız'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control m-3',
        'placeholder':'Email Adresiniz'
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control m-3',
        'placeholder':'Telefon Numaranız'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control m-3',
        'placeholder':'Mesajınız',
        'rows':'6'
    }))
    class Meta:
        model = Contact
        fields = ("firstName","lastName",'email','message')
