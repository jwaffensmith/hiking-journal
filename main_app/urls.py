from django.urls import path
from .views import Home, About, Profile

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('about/', About.as_view(), name="about"),
    path('profile/', Profile.as_view(), name="profile"),
]