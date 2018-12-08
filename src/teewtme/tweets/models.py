from django.db import models
from django.conf import settings
from .validators import content_not_empty
from django.urls import reverse

# Create your models here.
class Tweet(models.Model):
    user   = models.ForeignKey(settings.AUTH_USER_MODEL , default=1)
    content= models.CharField(max_length=140,validators=[content_not_empty])
    updated= models.DateField(auto_now=True)
    timestamp=models.DateField(auto_now_add=True)
    def get_absolute_url(self):
        return reverse("tweets:details" ,kwargs={"pk":self.pk})
