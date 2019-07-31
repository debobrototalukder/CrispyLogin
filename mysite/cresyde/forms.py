# from django import forms
# from django.contrib.auth.models import User
#
# from mysite.cresyde.models import UserProfileInfo
#
#
# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput())
#     country = forms.CharField()
#     class Meta():
#         model = User
#         fields = ('username', 'password', 'email')
#
#
# class UserProfileInfoForm(forms.ModelForm):
#     class Meta():
#         model = UserProfileInfo
#         fields = ('portfolio_site', 'profile_pic')
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Profile


class ProfileForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1']
        #fields = '__all__'


class ProfileExtraForm(forms.ModelForm):
    country = forms.CharField(required=True, widget=forms.TextInput(attrs={'required': "required"}))
    number = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'required': "required"}))

    class Meta:
        model = Profile
        exclude = ['fKey']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
