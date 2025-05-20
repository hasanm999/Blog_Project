from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import *
from django.views.generic import *

from .models import User


# Create your views here.
def login(request):
    return render(request, "register/login.html")


def register(request):
    return render(request, "register/register.html")


class Register(FormView):
    template_name = "register/register.html"
    form_class = RegistrationForm
    success_url = reverse_lazy('account:login')

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        phone_number = form.cleaned_data.get("phone_number")
        password1 = form.cleaned_data.get("password1")
        password2 = form.cleaned_data.get("password2")

        if password1 != password2:
            form.add_error('password2', "Passwords do not match!")
            return self.form_invalid(form)

        user = User.objects.create_user(
            username=username,
            phone_number=phone_number,
            password=password1
        )
        user.save()
        return super().form_valid(form)


class Login(LoginView):
    template_name = "register/login.html"
    form_class = LoginForm

    def get_success_url(self):
        return reverse_lazy('blog:index')


class Logout(LogoutView):
    next_page = reverse_lazy('blog:index')
