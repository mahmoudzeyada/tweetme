
from django.conf.urls import url,include
from .views import TweetListAPIView
from django.views.generic.base import RedirectView



urlpatterns = [

     #url (r"^$" , RedirectView.as_view(url="/")),
     url (r"^tweet/$" , TweetListAPIView.as_view(),name="list"),
    # url(r"^(?P<pk>\d+)/$",TweeteDetailView.as_view(),name="details"),
    # url(r"^create/$",TweetCreateView.as_view(),name="create"),
    # url(r"^(?P<pk>\d+)/update/$",TweetUpdateView.as_view(),name="update"),
    # url(r"^(?P<pk>\d+)/delete/$",TweetDeleteView.as_view(),name="delete"),

]
