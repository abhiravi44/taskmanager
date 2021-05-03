from django.apps import AppConfig


class ReportConfig(AppConfig):
    name = 'report'

    def ready(self):
        print(" ready triggered ")
        # from django.contrib.auth.models import User
        from .models import User
        from report.signals import create_profile
        from django.db.models.signals import post_save

        post_save.connect(create_profile,sender=User)
