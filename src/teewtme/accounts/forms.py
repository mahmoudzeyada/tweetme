from django import forms

from django.contrib.auth import get_user_model

class UserModelForm(forms.ModelForm):
    username=forms.CharField(required=True,max_length="150")
    password=forms.CharField(required=True)
    class Meta :
        model=get_user_model()
        fields=['username','password']
