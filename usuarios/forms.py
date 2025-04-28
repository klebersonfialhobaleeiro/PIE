from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):

    first_name = forms.CharField(
        max_length=30,
        required=True,
        label="Nome",
        help_text='Informe seu primeiro nome.',
        widget=forms.TextInput(attrs={'placeholder': 'Ex: João'})
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'password1', 'password2', 'is_superuser')
    
