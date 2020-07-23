from django.contrib import admin
from .models import FriendLink, MySiteData, BookLink, About, Home
# Register your models here.


@admin.register(FriendLink)
class FriendLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'link',)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc',)


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc',)


@admin.register(BookLink)
class BookLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'link',)


@admin.register(MySiteData)
class MySiteDataAdmin(admin.ModelAdmin):
    list_display = ('posts', 'categories', 'tags', 'readers', 'pageviews')
