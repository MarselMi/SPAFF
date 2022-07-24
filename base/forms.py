from .models import Client
from django.forms import ModelForm, TextInput


class ClientsForm(ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'surname', 'middle_name', 'email_adress', 'telephone_number', 'password']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            'surname': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'
            }),
            'middle_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Отчество'
            }),
            'email_adress': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес электронной почты'
            }),
            'telephone_number': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефона'
            }),
            'password': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Придумайте пароль'
            }),
        }