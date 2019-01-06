from rest_framework import generics
from .serializers import TweetModelsSerializer
from tweets.models import Tweet
class TweetListAPIView(generics.ListAPIView):
    serializer_class=TweetModelsSerializer
    def get_queryset(self,*args,**kwargs):
        return Tweet.objects.all()
