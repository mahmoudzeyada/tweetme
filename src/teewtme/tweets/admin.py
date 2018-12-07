from django.contrib import admin
from .models import Tweet
from .forms import TweetModelForm
# Register your models here.
#admin.site.register(Tweet)

class TweetModelAdmin(admin.ModelAdmin):
    class meta:
        model=Tweet


admin.site.register(Tweet, TweetModelAdmin)
