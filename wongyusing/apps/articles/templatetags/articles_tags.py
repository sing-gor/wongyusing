from django import template
from apps.articles import models
register = template.Library()




@register.simple_tag
def all_article_tags():
    return models.ArticleTags.objects.all()


@register.simple_tag
def all_article_categoies():
    return models.ArticleCategory.objects.all()






# @register.simple_tag
# def article_tag_single(pk):
#     return models.ArticleTags.objects.get(id=pk)


# @register.simple_tag
# def article_category_single(pk):
#     return models.ArticleCategory.objects.get(id=pk)
