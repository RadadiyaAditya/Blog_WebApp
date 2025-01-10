from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

#this file is use to customize the login or signup form by inheriting the already existing form

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    #this Meta class defines where to store the data from our form
    #by form.save() the data will be stored in following models provided in this class
    #here the user model is changed and the fields only specified here will be shown in the form
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profpic']