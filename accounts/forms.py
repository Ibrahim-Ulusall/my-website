from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Kullanıcı Adı'
    }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Parola'
    }))
    

class RegisterForm(forms.ModelForm):
    
    firstName = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Adınız'
    }))
    
    lastName = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Soyadınız'
    }))
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'E-posta Adresi'
    }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Parola'
    }))
    
    re_type_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Parola Tekrar'
    }))
    
    class Meta:
        model = User
        fields = ['firstName','lastName','email','password','re_type_password']