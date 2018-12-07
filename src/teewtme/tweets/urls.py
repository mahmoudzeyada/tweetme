
from django.conf.urls import url
from .views import TweetListView,TweeteDetailView,TweetCreateView,TweetUpdateView,TweetDeleteView



urlpatterns = [
    url (r"^$" , TweetListView.as_view(),name="list"),
    url(r"^(?P<pk>\d+)/$",TweeteDetailView.as_view(),name="details"),
    url(r"^create/$",TweetCreateView.as_view(),name="create"),
    url(r"^(?P<pk>\d+)/update/$",TweetUpdateView.as_view(),name="update"),
    url(r"^(?P<pk>\d+)/delete/$",TweetDeleteView.as_view(),name="delete")



]
