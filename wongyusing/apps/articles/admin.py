from django.contrib import admin
from apps.articles import models
# Register your models here.

@admin.register(models.Keywords)
class KeywordAdmin(admin.ModelAdmin):
    list_display = ('title','id',)


@admin.register(models.Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title','slug','data_status')

@admin.register(models.ArticleTags)
class ArticleTagsAdmin(admin.ModelAdmin):
    list_display = ('title','slug','data_status')

@admin.register(models.ArticleLogo)
class ArticleLogoAdmin(admin.ModelAdmin):
    list_display = ('title','img',)

@admin.register(models.ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ('title','slug','data_status')

# @admin.register(models.BlogTags)
# class BlogLinkTagAdmin(admin.ModelAdmin):
#     list_display = ('blog','blogtag',)

# @admin.register(BlogLinkLogo)
# class BlogLinkLogoAdmin(admin.ModelAdmin):
#     list_display = ('blog','bloglogo',)

# Register your models here.
