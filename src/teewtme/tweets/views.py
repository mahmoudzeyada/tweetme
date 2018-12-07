from django.shortcuts import render
from tweets.models import Tweet
from  django.views.generic import DetailView ,ListView , CreateView ,UpdateView,DeleteView
from .forms import TweetModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import UserRequiredMixin ,UserownerMixin
from django.urls import reverse_lazy
from django.db.models import Q

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
#create object
class TweetCreateView(CreateView,UserRequiredMixin,LoginRequiredMixin):
    model=Tweet
    fields=["content"]
    success_url="/tweet/create"
    template_name='tweets/create_view.html'
    login_url='admin/'
#update object
class TweetUpdateView(UserownerMixin,LoginRequiredMixin,UpdateView):
    model=Tweet
    form_class=TweetModelForm
    success_url=reverse_lazy("tweets:list")
    template_name='tweets/update_view.html'
    login_url='admin/'
#delete object
class TweetDeleteView(UserownerMixin,LoginRequiredMixin,DeleteView):
    model=Tweet
    form_class=TweetModelForm
    success_url=reverse_lazy("tweets:list")
login_url='admin/'
