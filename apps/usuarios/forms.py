from django import forms
from .models import Usuario

class LibroForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['titulo', 'autor', 'editoriales']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.Select(attrs={'class': 'form-control'}),  # Cambio el widget a Select
            'editoriales': forms.SelectMultiple(attrs={'class': 'form-control'}),  # Cambio el widget a SelectMultiple
        }
        

class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-user',
            'id': 'exampleInputEmail',
            'aria-describedby': 'emailHelp',
            'placeholder': 'Enter Email Address...',
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-user',
            'id': 'exampleInputPassword',
            'placeholder': 'Password',
        })
    )
