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
from django.forms import ModelForm

from .models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('country', 'pNumber')
