from django import forms
from .models import Tweet

class TweetModelForm (forms.ModelForm):
    content = forms.CharField(required=False,label="",
                            widget=forms.Textarea(
                            attrs={'placeholder':"your tweet",
                                    "class":"form-control"}
                            ))
    class Meta:
        model=Tweet
        fields=['content']
