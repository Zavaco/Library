from django import forms
from .models import LibUser, LibAdmin
from django.forms import ModelForm, DateTimeInput, SelectDateWidget
import datetime



class UserForm(forms.ModelForm):
    class Meta:
        model = LibUser
        fields = [
            'user_name',
            'email',
            'user_image',
            'password',
        ]
        widgets = {
                    'user_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name',
                                                        'id': 'validationCustom01'}),
                    'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your E-mail',
                                                     'id': 'validationCustomUsername'}),
                    'password': forms.TextInput(attrs={'class': 'form-control', 'id': 'validationCustom02',
                                                        'placeholder': 'Your password'}),


           }


class LibAdminForm(ModelForm):
    class Meta:
        model = LibAdmin
        fields = '__all__'

        widgets = {
            "take_date": DateTimeInput,

            "give_date": DateTimeInput,

        }
