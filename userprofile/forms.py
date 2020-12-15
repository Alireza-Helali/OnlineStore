from django.forms import ModelForm, TextInput, EmailInput, PasswordInput
from django.contrib.auth import get_user_model

user = get_user_model()


class RegisterForm(ModelForm):
    class Meta:
        model = user
        fields = {'username', 'email', 'password'}
        labels = {'username': 'نام کاربری(ضروری)',
                  'email': 'ایمیل(غیرضرورری)',
                  'password': 'کلمه عبور(ضروری)'}

        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری خود را وارد کنید'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'password': PasswordInput(attrs={'class': 'form-control'}),
        }

        help_texts = {
            'username': None,
            'email': None,
            'password': None
        }
