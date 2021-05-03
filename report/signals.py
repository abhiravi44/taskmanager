# from django.contrib.auth.models import User
from . models import Profile,User
from django.db.models.signals import post_save
from django.dispatch import receiver


def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
        print('profile created')


post_save(create_profile,sender=User)
