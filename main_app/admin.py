from django.contrib import admin
from .models import Hike, Profile, Comment

# Register your models here.
admin.site.register(Hike)
admin.site.register(Profile)
admin.site.register(Comment)