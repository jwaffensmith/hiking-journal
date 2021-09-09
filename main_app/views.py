from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import TemplateView
from .forms import SignupForm, ProfileForm
from .models import User 

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class Profile(TemplateView):
    template_name = "profile.html"

class Signup(TemplateView):
    
    template_name = "signup.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['signup_form'] = SignupForm()
        context['profile_form'] = ProfileForm()
        return context

    def post(self, request):
        signup_form = SignupForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if signup_form.is_valid() and profile_form.is_valid():
            user = signup_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect("/profile/")
        else: 
            context = {"signup_form": signup_form, "profile_form": profile_form}
            return render(request, "registration/signup.html", context)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
