from django import forms
from .models import Post, CustomUser
# from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post  
        fields = ['name', 'phone','email','style','image','content']

class SigninForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        help_texts = {
            'username': None,
        }
        fields = ['username','password']

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username','email','password','nickname','phone_number']