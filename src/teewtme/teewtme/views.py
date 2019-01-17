from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


def home (request):
    if request.user.is_authenticated():
        return render(request,"home.html")
    else:
        return HttpResponseRedirect(reverse("accounts:login"))
