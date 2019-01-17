from django import forms

from django.contrib.auth import get_user_model

class UserModelForm(forms.ModelForm):
    username=forms.CharField(required=True,max_length="150", widget=forms.TextInput(attrs={'placeholder': 'Username','class':'form-control'}))
    password=forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder': 'Password',"type":"password",'class':'form-control'}))
    class Meta :
        model=get_user_model()
        fields=['username','password']
