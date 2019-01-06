from rest_framework import serializers
from accounts.api.serializers import UserDisplaySerializer

from tweets.models import Tweet


class TweetModelsSerializer(serializers.ModelSerializer):
    user=UserDisplaySerializer()
    class Meta:
        model=Tweet
        fields=["user",
                "content"
                ]
