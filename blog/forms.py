from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    comidaFavorita = forms.CharField(label='Comida favorita', widget=forms.TextInput(attrs={'class':'form-control'}))
    localidad= forms.CharField(label='Localidad',widget=forms.TextInput(attrs={'class':'form-control'}))
    descripcion = forms.CharField(label='Descripcion',widget=forms.Textarea(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','comidaFavorita','localidad','descripcion']
        help_texts = {k:" " for k in fields}

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

        