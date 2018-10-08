from django import forms
from django.contrib.auth.models import User

class userForm(forms.ModelForm):
    password = forms.CharField(widget= forms.PasswordInput())
    #Above line is to make password not visible i.e. <input type="password">
    class Meta():
        model = User
        fields = ('username','email','password')
