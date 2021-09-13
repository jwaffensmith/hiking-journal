from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

handler404 = 'main_app.views.custom_page_not_found_view'
handler500 = 'main_app.views.custom_error_view'
handler403 = 'main_app.views.custom_permission_denied_view'
handler400 = 'main_app.views.custom_bad_request_view'
