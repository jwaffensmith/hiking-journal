from django.db import models
from django.db.models import Model, CharField, TextField, DateTimeField, ForeignKey, ImageField
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateField, IntegerField, DecimalField
from django.db.models.fields.files import ImageField
from django.contrib.auth.models import User


class Hike(Model):
    name = CharField(max_length=50)
    img_one = ImageField(max_length=500, default="https://images.pexels.com/photos/4448861/pexels-photo-4448861.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260")
    img_two = ImageField(max_length=500, blank= True)
    img_three = ImageField(max_length=500, blank= True)
    description = TextField(max_length=1000, blank= True)
    location = CharField(max_length=200)
    length = DecimalField(decimal_places=2, max_digits=7, default=0, blank= True)
    elevation_gain = IntegerField(default=0, blank= True)
    hike_rating = IntegerField(default=1)
    hike_date = DateField(auto_now=False, blank= True)
    created_at = DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return self.name
    
    class Meta: 
        ordering = ["-created_at"]


class Comment(Model):
    hike = ForeignKey(Hike, on_delete=CASCADE, related_name="comments")
    content = TextField(max_length=500)
    created_at = DateTimeField(auto_now_add=True)
    user = ForeignKey(User, on_delete=CASCADE, related_name="comments")

    def __str__(self):
        return f"{self.pk} - {self.hike.title}"



class Profile(Model):
    user = models.OneToOneField(User, on_delete=CASCADE, related_name="profile")
    avatar = CharField(max_length=400, default="https://source.unsplash.com/twukN12EN7c")
    location = CharField(max_length=100)

    def __str__(self):
        return self.user.username

