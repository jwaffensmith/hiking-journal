from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from .models import Profile, Hike

class UserCreationForm(UserCreationForm):
    first_name = forms.CharField(required=True, label='First Name')
    last_name = forms.CharField(required=True, label='Last Name')

    class Meta: 
        model = User
        fields = ("first_name", "last_name", "username", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user


class ProfileForm(forms.ModelForm):
        class Meta:
            model = Profile
            fields = ('location', 'avatar')


class HikeCreationForm(forms.ModelForm):
    class Meta:
        model = Hike
        template_name = "hike_create.html"
        fields= ["name", "img_one", "img_two", "img_three", "description", "location", "length", "elevation_gain", "hike_rating", "hike_date"]