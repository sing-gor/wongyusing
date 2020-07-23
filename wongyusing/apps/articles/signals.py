from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.articles.models import ArticleTags, ArticleCategory, Articles
from apps.mysite.models import MySiteData


@receiver(post_save, sender=Articles)
def articles_count(sender, instance, created, **kwargs):

    postsNum = Articles.objects.filter(data_status=0).count()
    site_data = MySiteData.objects.filter(pk=1)[0]
    site_data.posts = postsNum
    site_data.save()


@receiver(post_save, sender=ArticleTags)
def blog_tags_count(sender, instance, created, **kwargs):

    postsNum = ArticleTags.objects.all().count()
    site_data = MySiteData.objects.filter(pk=1)[0]
    site_data.tags = postsNum
    site_data.save()


@receiver(post_save, sender=ArticleCategory)
def blog_category_count(sender, instance, created, **kwargs):

    postsNum = ArticleCategory.objects.all().count()
    site_data = MySiteData.objects.filter(pk=1)[0]
    site_data.categories = postsNum
    site_data.save()
