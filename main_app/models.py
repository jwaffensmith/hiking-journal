import time

from django.db import models
from django.db.models import Model, CharField, TextField, DateTimeField, ForeignKey, ImageField
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateField, IntegerField, DecimalField
from django.db.models.fields.files import ImageField


# Create your models here.
class Hike(Model):
    name = CharField(max_length=50)
    img = ImageField(max_length=600, default="https://images.pexels.com/photos/4448861/pexels-photo-4448861.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260")
    description = TextField(max_length=1000)
    location = CharField(max_length=200)
    length = DecimalField(decimal_places=2, max_digits=7, default=0)
    elevation_gain = IntegerField(default=0)
    hike_rating = IntegerField(default=1)
    hike_date = DateField(auto_now=False)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def get_length(self):
        return time.strftime("%-M:%S", time.gmtime(self.length))

    class Meta: 
        ordering = ["created_at"]



class Comment(Model):
    hike = ForeignKey(Hike, on_delete=CASCADE, related_name="comments")
    content = CharField(max_length=200)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pk} - {self.hike.title}"



class Profile(Model):
    username = CharField(max_length=30)
    avatar = CharField(max_length=200, default="https://source.unsplash.com/twukN12EN7c")
    location = CharField

