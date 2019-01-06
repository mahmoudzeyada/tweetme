from django.shortcuts import render
from tweets.models import Tweet
from  django.views.generic import DetailView ,ListView , CreateView ,UpdateView,DeleteView
from .forms import TweetModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import UserRequiredMixin ,UserownerMixin
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm


#details for object
class TweeteDetailView(DetailView):
    model=Tweet

#list objects
class TweetListView(ListView):
    model=Tweet
    def get_queryset(self,*args,**kargws):
        qs=super().get_queryset()
        search_word=self.request.GET.get("search_word")
        if search_word is not None:
            qs=qs.filter(Q(content__icontains=search_word)|
                        Q(user__username__icontains=search_word))

        return qs
    def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         context["create_form"]=TweetModelForm()
         context["create_url"]=reverse_lazy("tweets:create")
         return context

#create object
class TweetCreateView(LoginRequiredMixin,UserRequiredMixin,CreateView):
    model=Tweet
    form_class=TweetModelForm

    #success_url=reverse_lazy("tweets:details")
    template_name='tweets/create_view.html'
    login_url='/accounts/login/'
   
    
#update object
class TweetUpdateView(LoginRequiredMixin,UserownerMixin,UpdateView):
    model=Tweet
    form_class=TweetModelForm
    #success_url=reverse_lazy("tweets:details")
    template_name='tweets/update_view.html'
    login_url='admin/'
#delete object
class TweetDeleteView(LoginRequiredMixin,UserownerMixin,DeleteView):
    model=Tweet
    form_class=TweetModelForm
    success_url=reverse_lazy("tweets:list")
    login_url='admin/'
#resgstration object

class Registeration (CreateView):
    template_name='registration/register.html'
    form_class=UserCreationForm
    success_url=reverse_lazy('sucess_register')
