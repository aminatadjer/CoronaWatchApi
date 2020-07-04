from django.apps import AppConfig


class AuthConfig(AppConfig):
    name = 'customauth'
    def ready(self):
        from customauth.group import group_perms
        group_perms()