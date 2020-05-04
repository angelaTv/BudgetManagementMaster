from django import forms
from django.forms import ModelForm

from accounts.models import Users


class UserCreationForm(ModelForm):
    class Meta:
        model = Users
        fields = '__all__'


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=120)
    password = forms.CharField(max_length=120, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        if Users.objects.filter(username=username):
            pass
        else:
            msg = "no user exist in this name"
            self.add_error('username', msg)
