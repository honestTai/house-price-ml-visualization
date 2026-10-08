from django.apps import AppConfig


class SitesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'houses'


class TasksConfig(AppConfig):
    name = 'houses'

    verbose_name = '房屋数据'
