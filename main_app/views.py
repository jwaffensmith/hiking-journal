from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from .forms import UserCreationForm, ProfileForm
from .models import Hike, User, Profile, Comment
from django.contrib import messages

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class ProfileRedirect(View):
    def get(self, request):
        return redirect(f"/profile/{request.user.profile.pk}")

class Signup(View):
    def get(self, request):
        signup_form = UserCreationForm()
        profile_form = ProfileForm()
        context = {"signup_form": signup_form, "profile_form": profile_form}
        return render(request, "registration/signup.html", context)

    def post(self, request):
        signup_form = UserCreationForm(request.POST)
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
        fields = ("username", "password1", "password2")


class ProfileDetail(TemplateView):
    model = Profile
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(pk=self.kwargs.get("pk"))
        context['hikes'] = Hike.objects.filter(user=self.kwargs.get("pk"))
        context['comments'] = Comment.objects.filter(user=self.kwargs.get("pk"))
        return context

class HikeDetail(DetailView):
    model = Hike
    template_name = "hike_detail.html"

class HikeCreate(CreateView):
    model = Hike
    template_name = "hike_create.html"
    fields= ["name", "img_one", "img_two", "img_three", "description", "location", "length", "elevation_gain", "hike_rating", "hike_date"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.Profile = Profile.objects.get(pk=self.kwargs.get("pk"))
        return super(HikeCreate, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, self.error_message)
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse("hike_detail", kwargs={'pk': self.object.pk})


class HikeUpdate(UpdateView):
    model = Hike
    fields= ["name", "img_one", "img_two", "img_three", "description", "location", "length", "elevation_gain", "hike_rating", "hike_date"]
    template_name = "hike_update.html"

    def get_success_url(self):
        return reverse("hike_detail", kwargs={"pk": self.object.pk})


class HikeDelete(DeleteView):
    model = Hike
    success_url = reverse("profile")
