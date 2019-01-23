from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from .views import home
from tweets.views import TweetListView
#from tweets.views import Registeration
from django.views.generic import TemplateView

urlpatterns = [
    url (r"^$" , TweetListView.as_view(),name="home"),
    url(r'^admin/', admin.site.urls),
    url(r"^tweet/",include('tweets.urls',namespace="tweets")),
    url(r"^api/",include('tweets.api.urls',namespace="api")),
    url (r"^accounts/",include('accounts.urls',namespace="accounts"))
    #url(r"^accounts/",include('django.contrib.auth.urls')),
    #url(r"^registration/",Registeration.as_view(),name="register"),
    #url(r"^registration/sucess/",TemplateView.as_view(template_name="registration/register_sucess.html"),name='sucess_register')


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
