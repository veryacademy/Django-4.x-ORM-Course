from django.apps import AppConfig
from django.contrib.auth import get_user_model


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'

    def sayhi(self):
        print("hiya")

    def ready(self):
        User = get_user_model()
        User.sayhi = self.sayhi