from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_reset/password_change_done.html'), 
        name='password_change_done'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_reset/password_change.html'), 
        name='password_change'),
    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_done.html'),
    name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_complete.html'),
    name='password_reset_complete'),
]

handler404 = 'main_app.views.custom_page_not_found_view'
handler500 = 'main_app.views.custom_error_view'
handler403 = 'main_app.views.custom_permission_denied_view'
handler400 = 'main_app.views.custom_bad_request_view'
