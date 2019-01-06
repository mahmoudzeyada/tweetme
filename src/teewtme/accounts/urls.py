from django.conf.urls import url,include
from . import views
from django.views.generic.base import TemplateView

urlpatterns=[
    url(r"^login/",views.login_user,name="login"),
    url (r"^register/",views.regstier,name="register"),
   url(r"^sucess/",TemplateView.as_view(template_name="registration/register_sucess.html"),name='register_sucess'),
   url(r"^logout/",views.user_logout,name="logout")
]