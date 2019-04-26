from django.db import models
from django.conf import settings
from .validators import content_not_empty
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Tweet(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE
                             )
    content = models.CharField(max_length=140, validators=[content_not_empty])
    updated = models.DateField(auto_now=True)
    timestamp = models.DateField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse("tweets:details", kwargs={"pk": self.pk})
