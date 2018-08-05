from django import forms
from django.contrib.auth.models import User
from user.models import UserProfile, Picture


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')


class UserProfile(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('profile_pic',)


class PictureForm(forms.Form):
    class Meta:
        model = Picture
        fields = ('picture',)
