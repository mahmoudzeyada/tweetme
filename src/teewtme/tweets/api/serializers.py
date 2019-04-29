from rest_framework import serializers
from accounts.api.serializers import UserDisplaySerializer
from django.contrib.auth import get_user_model
from django.utils.timesince import timesince
from tweets.models import Tweet
from rest_framework.fields import CurrentUserDefault
from django.urls import reverse_lazy


class TweetModelsSerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer(read_only=True)
    date_display = serializers.SerializerMethodField()
    time_since = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()

    class Meta:
        model = Tweet
        fields = ["user", "content", "timestamp",
                  "date_display", "time_since", "url"]
        read_only_fields = ["timestamp"]

    def get_date_display(self, obj):
        return obj.timestamp.strftime("%b %d , %I:%M %p")

    def get_time_since(self, obj):
        return timesince(obj.timestamp)

    def get_url(self, obj):
        return reverse_lazy(
            "accounts:userdetails",
            kwargs={"username": obj.user.username}
        )
