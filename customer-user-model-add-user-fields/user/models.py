from django.db import models
from django.contrib.auth.admin import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)
    nickname = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

# class PersonManagerInactive(models.Manager):
#     def get_queryset(self):
#         return super(PersonManagerInactive, self).get_queryset().filter(is_active=False)

# class PersonManagerActive(models.Manager):
#     def get_queryset(self):
#         return super(PersonManagerActive, self).get_queryset().filter(is_active=True)

# class Person(User):

#     inactive = PersonManagerInactive()
#     active = PersonManagerActive()

#     class Meta:
#         proxy = True
#         ordering = ('first_name',)

#     @classmethod
#     def count_all(cls,):
#         return cls.objects.filter(is_active=True).count()

#     def check_active(self):
#         if self.is_active == True:
#             return "You are Active!"
#         else:
#             return "You are not Active!"

#     def __str__(self):
#         return self.first_name

