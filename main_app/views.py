from django.views.generic.base import TemplateView

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class Profile(TemplateView):
    template_name = "profile.html"
