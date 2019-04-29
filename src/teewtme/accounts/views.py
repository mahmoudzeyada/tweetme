from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .forms import UserModelForm


class UserDetails(DetailView):
    model = get_user_model()
    template_name = "accounts/user_details.html"
    context_object_name = "user"

    def get_object(self, queryset=None):
        return get_object_or_404(
            self.model,
            username__iexact=self.kwargs.get("username")
        )

# login


def login_user(request):
    form = UserModelForm()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("home"))
            else:
                return HttpResponse("Your account is not active")
        else:
            return HttpResponse("invaild username or password")
    else:
        return render(request, "registration/login.html", {"form": form})

# register


def regstier(request):
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Acoount created successfully')
            return HttpResponseRedirect(reverse_lazy('accounts:register_sucess'))
        else:
            return render(request, "registration/register.html", {"form": form})

    else:
        form = UserCreationForm()
        return render(request, "registration/register.html", {"form": form})
# log_out
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("accounts:login"))
