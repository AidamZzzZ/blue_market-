from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import CustomUser

@receiver(post_save, sender=CustomUser)
def add_user_to_students_group(sender, instance, created, **kwargs):
    if created:
        try:
            basics = Group.objects.get(name='basic')
        except Group.DoesNotExist:
        	basics = Group.objects.create(name='basic')
        	basics = Group.objects.create(name='advanced')
        	basics = Group.objects.create(name='administrative')
        instance.groups.add(basics)





