from django.contrib import admin

# Register your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import *

admin.site.register(BaseUser)
admin.site.register(Right)
admin.site.register(RightByAccess)
admin.site.register(UserRight)
admin.site.register(Role)
admin.site.register(UserRole)
admin.site.register(RoleRight)


@receiver(post_save, sender=BaseUser)
def my_handler(sender, instance, created, **kwargs):
    if created:
        for right in RightByAccess.objects.all():
            user_right = UserRight.objects.filter(user=instance.id, right=right.id).first()
            if not user_right:
                user_right = UserRight(
                    user=instance,
                    right=right
                )
                user_right.save()