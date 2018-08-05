from django.db import models
from django.contrib.auth.models import  User
# Create your models here.


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # additional field in User Model

    profile_pic = models.URLField(blank=True)

    def __str__(self):
        return self.user.username


class Picture(models.Model):

   picture = models.ImageField(upload_to = 'pictures')

   class Meta:

      db_table = "picture"