from rest_framework import generics
from .serializers import TweetModelsSerializer
from tweets.models import Tweet
from django.db.models import Q
class TweetListAPIView(generics.ListAPIView):
    serializer_class=TweetModelsSerializer
    def get_queryset(self):
        queryset=Tweet.objects.all()
        search=self.request.query_params.get('search',None)
        print(search)
        if search != "Null":
            
            print("phase1")
            queryset=queryset.filter(Q(content__icontains=search)|
                        Q(user__username__icontains=search))


        return queryset
