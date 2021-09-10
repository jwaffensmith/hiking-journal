from django.urls import path
from .views import Home, About, Signup, ProfileDetail, ProfileRedirect, HikeCreate, HikeDetail

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('about/', About.as_view(), name="about"),
    path('profile/', ProfileRedirect.as_view(), name="profile_redirect"),
    path('profile/<int:pk>/', ProfileDetail.as_view(), name="profile"),
    path('accounts/signup/', Signup.as_view(), name="signup"),
    path('profile/<int:pk>/hike/new/', HikeCreate.as_view(), name="hike_create"),
    path('hikes/<int:pk>/', HikeDetail.as_view(), name="hike_detail"),
]