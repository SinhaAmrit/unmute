from email.policy import default
import imp
from statistics import mode
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.db.models.signals import post_save


def user_director_path(instance, filename):
    return "user_{0}/{1}".format(instance.user.id, filename)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    bio = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to=user_director_path, default="default.png"
    )
    website = models.URLField(default="https://www.website.com/")
    facebook = models.URLField(default="https://www.facebook.com/")
    instagram = models.URLField(default="https://www.instagram.com/")
    twitter = models.URLField(default="https://www.twitter.com/")

    def __str__(self):
        try:
            return f"{self.full_name} - {self.user.username} - {self.user.email}"
        except:
            return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
