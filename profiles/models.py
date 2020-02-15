from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, default='', blank=True)
    birthdate = models.DateField(null=True, blank=True)
    teacher = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='images/users/', null=True, blank=True)
    website = models.URLField(default='', blank=True)
    phone = models.CharField(max_length=20, blank=True, default='')

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

