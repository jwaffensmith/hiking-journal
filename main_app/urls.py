from django.urls import path
from .views import Home, About, Profile, Signup

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('about/', About.as_view(), name="about"),
    path('profile/', Profile.as_view(), name="profile"),
    path('accounts/signup/', Signup.as_view(), name="signup"),
]