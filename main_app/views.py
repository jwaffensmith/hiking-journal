from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from .forms import UserCreationForm, ProfileForm, UpdateProfileForm, UpdateUserForm
from django.db.models.functions import Concat
from django.db.models import Value as V
from .filters import HikeFilter
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
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

@method_decorator(login_required, name='dispatch')
class ProfileDetail(DetailView):
    model = Profile
    template_name = "profile/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hikes'] = Hike.objects.filter(user=self.request.user)
        context['profile'] = Profile.objects.get(pk=self.kwargs.get("pk"))
        context['comments'] = Comment.objects.filter(user=self.kwargs.get("pk"))
        return context

@method_decorator(login_required, name='dispatch')
class SearchView(View):
    template_name = 'search/search.html'

    def get(self, request):
       return render(request, "search/search.html", {})

    def post(self, request):
        if request.method == "POST":
            searched = request.POST['searched']
            hikes = Hike.objects.filter(name__icontains=searched)
            users = User.objects.annotate(full_name=Concat('first_name', V(' '), 'last_name')).\
                filter(full_name__icontains=searched)
            return render(request, 'search/search.html', {'searched': searched, 'hikes': hikes, 'users': users})
        else: 
            return render(request, "search/search.html", {})

@method_decorator(login_required, name='dispatch')
class ProfileUpdate(TemplateView):
    template_name = "profile/profile_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        user = get_object_or_404(User, pk=profile.user.pk)
        print("User pk", user.pk)
        print("profile pk", profile.pk)
        context['profile'] = profile
        context['user'] = user
        context['update_profile_form'] = UpdateProfileForm(instance=profile)
        context['update_user_form'] = UpdateUserForm(instance=user)
        return context

    def post(self, request, *args, **kwargs):   
        profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        user = get_object_or_404(User, pk=profile.user.pk)

        update_profile_form = UpdateProfileForm(instance=profile, data=request.POST)
        update_user_form = UpdateUserForm(instance=user, data=request.POST)

        if update_profile_form.is_valid() and update_user_form.is_valid():
            update_profile_form.save()
            update_user_form.save()
            return redirect("/profile/")
        else:
            context = {"update_user_form": update_user_form, 
            "update_profile_form": update_profile_form }
            return render(request, "profile/profile_update.html", context)

@method_decorator(login_required, name='dispatch')
class HikeDetail(DetailView):
    model = Hike
    template_name = "hike/hike_detail.html"

@method_decorator(login_required, name='dispatch')
class HikeCreate(CreateView):
    model = Hike
    template_name = "hike/hike_create.html"
    fields= ["name", "img_one", "img_two", "img_three", "location", "hike_date", "length", "elevation_gain", "hike_rating",  "description"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.Profile = Profile.objects.get(pk=self.kwargs.get("pk"))
        return super(HikeCreate, self).form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse("hike_detail", kwargs={'pk': self.object.pk})

@method_decorator(login_required, name='dispatch')
class HikeUpdate(UpdateView):
    model = Hike
    fields= ["name", "img_one", "img_two", "img_three", "location", "hike_date", "length", "elevation_gain", "hike_rating",  "description"]

    def get_success_url(self):
        return reverse("hike_detail", kwargs={"pk": self.object.pk})

@method_decorator(login_required, name='dispatch')
class HikeDelete(View):
    def post(self, request, pk):
        hike_to_delete = Hike.objects.get(id=pk)
        hike_to_delete.delete()
        return redirect("/profile/")

@method_decorator(login_required, name='dispatch')
class CommentCreate(CreateView):
    def post(self, request, pk, hike_pk):
        comment_content = request.POST.get("content")
        related_hike = Hike.objects.get(id=hike_pk)
        Comment.objects.create(content=comment_content, hike=related_hike, user=request.user)
        return redirect(f"/profile/{pk}")

@method_decorator(login_required, name='dispatch')
class CommentDetail(DetailView):
        model = Comment
        template_name= "comment/comment_detail.html"

@method_decorator(login_required, name='dispatch')
class CommentUpdate(UpdateView):
    model = Comment
    fields = ["content"]

    def get_success_url(self):
        return reverse("comment_detail", kwargs={"pk": self.object.pk})

@method_decorator(login_required, name='dispatch')       
class CommentDelete(View):
    def post(self, request, pk):
        comment_to_delete = Comment.objects.get(id=pk)
        comment_to_delete.delete()
        return redirect("/profile/")
        
@method_decorator(login_required, name='dispatch')
class SortView(TemplateView):
    template_name = 'search/sort_hikes.html'

    def get(self, request):
        hikes = Hike.objects.filter(user=request.user)
        hike_filter = HikeFilter(request.GET, queryset=hikes)
        hikes = hike_filter.qs
        context = {'hikes': hikes, 'hike_filter': hike_filter}
        return render(request, "search/sort_hikes.html", context)

def custom_page_not_found_view(request, exception):
    return render(request, "errors/404.html", {})

def custom_error_view(request, exception=None):
    return render(request, "errors/500.html", {})

def custom_permission_denied_view(request, exception=None):
    return render(request, "errors/403.html", {})

def custom_bad_request_view(request, exception=None):
    return render(request, "errors/400.html", {})