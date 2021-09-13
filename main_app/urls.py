from django.urls import path
from .views import Home, About, Signup, ProfileDetail, ProfileRedirect, HikeCreate, HikeDetail, HikeUpdate, HikeDelete, CommentDetail, CommentCreate, CommentDelete, CommentUpdate, ProfileUpdate, SearchView, SortView

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('about/', About.as_view(), name="about"),
    path('profile/', ProfileRedirect.as_view(), name="profile_redirect"),
    path('profile/<int:pk>/', ProfileDetail.as_view(), name="profile"),
    path('profile/<int:pk>/update', ProfileUpdate.as_view(), name="profile_update"),
    path('accounts/signup/', Signup.as_view(), name="signup"),
    path('profile/<int:pk>/hike/new/', HikeCreate.as_view(), name="hike_create"),
    path('hikes/<int:pk>/', HikeDetail.as_view(), name="hike_detail"),
    path('hikes/<int:pk>/update/', HikeUpdate.as_view(), name="hike_update"),
    path('hikes/<int:pk>/delete/', HikeDelete.as_view(), name="hike_delete"),
    path('profile/<int:pk>/hike/<int:hike_pk>/comments/new/', CommentCreate.as_view(), name="comment_create"),
    path('comments/<int:pk>/', CommentDetail.as_view(), name="comment_detail"),
    path('comments/<int:pk>/update/', CommentUpdate.as_view(), name="comment_update"),
    path('comments/<int:pk>/delete/', CommentDelete.as_view(), name="comment_delete"),
    path('search/', SearchView.as_view(), name="search"),
    path('sorthikes/', SortView.as_view(), name="sort_hikes")
]
