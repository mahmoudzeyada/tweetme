from django.shortcuts import render, get_object_or_404
from tweets.models import Tweet , Like
from  django.views.generic import DetailView ,ListView , CreateView ,UpdateView,DeleteView
from .forms import TweetModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import UserRequiredMixin ,UserownerMixin
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.views import View
#details for object
class TweeteDetailView(DetailView):
    model=Tweet

#list objects
class TweetListView(LoginRequiredMixin,ListView):
    model=Tweet
    login_url='/accounts/login/'
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
class TweetDeleteView(DeleteView):
    model=Tweet
    form_class=TweetModelForm
    success_url=reverse_lazy("tweets:list")
    login_url='admin/'
    def delete(self,request,*args,**kwargs):
        self.object=self.get_object()
        not_user=False
        if self.object.user == self.request.user :
            return super().delete(self,request,*args,**kwargs)
        else:
            not_user=True
            return render(request,"tweets/tweet_confirm_delete.html",{"object":self.object,"not_user":not_user})

class PreferanceView(View):

    template_name="tweets/test.html"
    def get (self,request,*args,**kwargs):
        tweet_id=self.kwargs["tweet_id"]
        tweet=get_object_or_404(Tweet,id=tweet_id)
        return render(request,self.template_name,{"tweet":tweet})


    def post(self,request,*args,**kwargs):
        tweet_id=self.kwargs["tweet_id"]
        type_like =int(self.kwargs["type_like"])
        tweet=get_object_or_404(Tweet,id=tweet_id)
        try:
            like=Like.objects.get(user=request.user,tweet=int(tweet_id))
            model_type_like =like.type_like
            if type_like  != model_type_like  :
                like.delete()
                user_like=Like()
                user_like.user=request.user
                user_like.tweet=tweet
                user_like.type_like=type_like 
                if type_like ==1 and model_type_like !=1 :
                    tweet.likes+=1
                    tweet.dislikes-=1
                elif type_like ==2 and model_type_like !=2:
                    tweet.likes-=1
                    tweet.dislikes+=1
                user_like.save()
                tweet.save()
                return render(request,self.template_name,{"tweet":tweet})
            elif type_like  == model_type_like  :
                like.delete()
                if type_like == 1 :
                    tweet.likes-=1
                elif type_like == 2:
                    tweet.dislikes -=1
                tweet.save()
                return render(request,self.template_name,{"tweet":tweet})
        except Like.DoesNotExist:
            like=Like()
            like.user=request.user
            like.tweet=tweet
            like.type_like=type_like 
            if type_like ==1 :
                tweet.likes+=1
            elif type_like  ==2 :
                tweet.dislikes+=1
            like.save()
            tweet.save()
            return render(request,self.template_name,{"tweet":tweet})
        

            


        
        





