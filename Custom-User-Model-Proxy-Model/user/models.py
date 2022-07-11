from django.db import models
from django.contrib.auth.admin import User

class PersonManagerInactive(models.Manager):
    def get_queryset(self):
        return super(PersonManagerInactive, self).get_queryset().filter(is_active=False)

class PersonManagerActive(models.Manager):
    def get_queryset(self):
        return super(PersonManagerActive, self).get_queryset().filter(is_active=True)

class Person(User):

    inactive = PersonManagerInactive()
    active = PersonManagerActive()

    class Meta:
        proxy = True
        ordering = ('first_name',)

    @classmethod
    def count_all(cls,):
        return cls.objects.filter(is_active=True).count()

    def check_active(self):
        if self.is_active == True:
            return "You are Active!"
        else:
            return "You are not Active!"

    def __str__(self):
        return self.first_name

