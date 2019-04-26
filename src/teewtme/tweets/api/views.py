from rest_framework import generics
from rest_framework import permissions
from .serializers import TweetModelsSerializer
from tweets.models import Tweet
from django.db.models import Q


class TweetListAPIView(generics.ListAPIView, generics.CreateAPIView):
    # permission_class=[permissions.IsAuthenticated]
    serializer_class = TweetModelsSerializer

    def get_queryset(self):
        queryset = Tweet.objects.all().order_by("-id")
        search = self.request.query_params.get('search', None)
        # print(search)
        if search != "Null" and search is not None:

            # print("phase1")
            queryset = queryset.filter(Q(content__icontains=search) |
                                       Q(user__username__icontains=search))

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
