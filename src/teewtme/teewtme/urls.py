
from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from .views import home
from tweets.views import TweetListView
urlpatterns = [
    url (r"^$" , TweetListView.as_view(),name="home"),
    url(r'^admin/', admin.site.urls),
    url(r"^tweet/",include('tweets.urls',namespace="tweets"))

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
