from django import forms
from .models import Tweet
from django.contrib.auth import get_user_model

class TweetModelForm (forms.ModelForm):
    content = forms.CharField(required=False,label="",
                            widget=forms.Textarea(
                            attrs={'placeholder':"your tweet",
                                    "class":"form-control"}
                            ))
    
    class Meta:
        model=Tweet
        fields=['content']
    def clean_content(self,*args,**kwargs):
        content = self.cleaned_data.get("content")
        if content=="bitch":
            raise forms.ValidateError("you r the fqin bitch")
        return content
