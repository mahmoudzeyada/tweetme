from django.db import models
from django.conf import settings
from .validators import content_not_empty
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Tweet(models.Model):
    
    user   = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    content= models.CharField(max_length=140,validators=[content_not_empty])
    updated= models.DateField(auto_now=True)
    timestamp=models.DateField(auto_now_add=True)
    likes=models.IntegerField(default=0)
    dislikes=models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse("tweets:details" ,kwargs={"pk":self.pk})
class Like (models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    tweet = models.ForeignKey(Tweet)
    created=models.DateField(auto_now=True)
    type_like = models.IntegerField(null=True)

    def __str__(self):
        return str(self.user)+":"+str(self.tweet)+':'+str(self.type_like)
    class Meta:
        unique_together=("user","tweet","type_like")
