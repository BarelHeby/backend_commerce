from django import forms
from users.models import user


class userForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ["name", "phone_number", "email"]
