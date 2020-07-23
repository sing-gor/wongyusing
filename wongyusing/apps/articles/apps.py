from django.apps import AppConfig


class ArticlesConfig(AppConfig):
    name = 'apps.articles'
    label = 'articles'

    def ready(self):
        from apps.articles import signals
